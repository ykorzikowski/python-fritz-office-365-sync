# -*- coding: utf-8 -*-
import os

from O365 import Account, Connection
from datetime import datetime as dt
from datetime import timedelta
from conf.conf import CONFIG as conf
from fritzhome import FritzBox
import logging

class Core(object):
    def run(self):
        logging.basicConfig(level=logging.INFO)
        credentials = (conf['OFFICE_CLIENT_ID'], conf['OFFICE_CLIENT_SECRET'])
        scopes = ['offline_access',
                  'https://graph.microsoft.com/Mail.ReadWrite',
                  'https://graph.microsoft.com/Mail.Send',
                  'https://graph.microsoft.com/Calendars.Read',
                  'https://graph.microsoft.com/Files.ReadWrite',
                  'https://graph.microsoft.com/User.Read']

        con = Connection(credentials, scopes=scopes)

        if not con.check_token_file():
            self.gen_token_file(con)

        heating = self.query_for_heating_periods(credentials)

        # Cool down if no heating entries found in calendar
        if len(heating) == 0:
            logging.debug('No heating entry in calendar found. Cooling down all thermostats if they are heating. ')
            self.cool_down()

        # For each heating entry in calendar heat up
        for heat in heating:
            logging.info('Found entry "%s"', heat.subject)
            self.heat_up(heat.subject)

        # Every night refresh the token
        if dt.now().time().strftime('%H:%M') == '00:00':
            con.refresh_token()

    """
    Gets all thermostats from fritzbox
    """
    def get_thermostats(self):
        if conf['FRITZ_TLS']:
            fritzbox = FritzBox(conf['FRITZ_IP'],  conf['FRITZ_USER'], conf['FRITZ_PW'], use_tls=conf['FRITZ_TLS'], tls_cert_path='conf/fritz.crt')
        else:
            fritzbox = FritzBox(conf['FRITZ_IP'],  conf['FRITZ_USER'], conf['FRITZ_PW'], use_tls=conf['FRITZ_TLS'])
        fritzbox.login()
        actors = fritzbox.get_actors()
        thermostats = []
        for actor in actors:
            if actor.has_heating_controller:
                thermostats.append(actor)

        return thermostats

    def thermostat_heatup(self, actor):
        logging.info('Heating up %s ...', actor.name)
        actor.set_temperature(conf['HEATING_COMFORT_TEMP'])

    """
    Sets the temperature of thermostats with matching subject or all thermostats to comfort temperature
    """
    def heat_up(self, sub):
        thermostats = self.get_thermostats()
        for thermostat in thermostats:
            if sub == conf['CALENDAR_HEAT_ALL_SUBJECT']:
                self.thermostat_heatup(thermostat)
            else:
                if thermostat.name == sub:
                    self.thermostat_heatup(thermostat)

    """
    Sets the temperature of all thermostats to LOW_TEMP if they are currently set to COMFORT_TMEP
    """
    def cool_down(self):
        thermostats = self.get_thermostats()
        for thermostat in thermostats:
            if thermostat.target_temperature == conf['HEATING_COMFORT_TEMP']:
                logging.info('Cooling down %s ...', thermostat.name)
                thermostat.set_temperature(conf['HEATING_LOW_TEMP'])

    """
    If the temperature has changed manually via app or on the thermostat itself, 
    this method resets the temperature to the HEATING_LOW_TEMP on a given time
    """
    def auto_reset(self):
        if conf['HEATING_AUTO_RESET']:
            current_time = dt.now().time()
            target_time = conf['HEATING_AUTO_RESET_TIME']

            if current_time.strftime('%H:%M') == target_time:
                logging.info('Resetting temperature on all thermostats now!')
                thermostats = self.get_thermostats()
                for thermostat in thermostats:
                    thermostat.set_temperature(conf['HEATING_LOW_TEMP'])

    def query_for_heating_periods(self, credentials):
        account = Account(credentials=credentials)
        schedule = account.schedule()
        calendar = schedule.get_calendar(calendar_name=conf['CALENDAR_NAME'])

        if calendar is None:
            logging.error("Calendar with name '%s' does not exist!", conf['CALENDAR_NAME'])
            exit(1)

        q = calendar.new_query('start').greater_equal(dt.now())
        q.chain('and').on_attribute('end').less_equal(dt.now() + timedelta(minutes=5))

        return calendar.get_events(query=q)

    def gen_token_file(self, con):
        print("No valid token found. Starting authentication process...")
        print("Please visit the following url and paste the result url into the cli!")
        url = con.get_authorization_url()
        print(url)
        result_url = input('Paste the result url here...')
        con.request_token(result_url)

if __name__ == "__main__":
    Core().run()