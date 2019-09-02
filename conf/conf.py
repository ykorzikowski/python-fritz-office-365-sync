# python-fritz-office-365-sync settings
import os

CONFIG_DOCKER = {
    # Only hostname or ip. No http or www
    'FRITZ_IP': os.getenv('FRITZ_IP', 'fritz.box'),
    'FRITZ_USER': os.getenv('FRITZ_USER', 'fritzctl'),
    'FRITZ_PW': os.getenv('FRITZ_PW', 'mypw'),
    # If you are using https, be sure to store the self signed certificate of the fritzbox in the path conf/fritz.crt
    'FRITZ_TLS': os.getenv('FRITZ_TLS', 'false'),

    # the office app to configure
    'OFFICE_CLIENT_ID': os.getenv('OFFICE_CLIENT_ID',''),
    'OFFICE_CLIENT_SECRET': os.getenv('OFFICE_CLIENT_SECRET',''),

    # The calendar to query
    'CALENDAR_NAME': os.getenv('CALENDAR_NAME', 'Heizen'),

    # Subject that will cause all radiators to heat for the given event time
    'CALENDAR_HEAT_ALL_SUBJECT': os.getenv('CALENDAR_HEAT_ALL_SUBJECT', 'Heizen'),

    # The comfort and low temperature
    'HEATING_COMFORT_TEMP': os.getenv('HEATING_COMFORT_TEMP', '21'),
    'HEATING_LOW_TEMP': os.getenv('HEATING_LOW_TEMP', '16'),

    # To reset changes made directly at the thermostat or via app
    'HEATING_AUTO_RESET': os.getenv('HEATING_AUTO_RESET', 'true'),
    'HEATING_AUTO_RESET_TIME': os.getenv('HEATING_AUTO_RESET_TIME', '00:00')
}

CONFIG_NODOCKER = {
    # Only hostname or ip. No http or www
    'FRITZ_IP': '${FRITZ_IP|fritz.box}',
    'FRITZ_USER': 'fritzctl',
    'FRITZ_PW': 'mypw',
    # If you are using https, be sure to store the self signed certificate of the fritzbox in the path conf/fritz.crt
    'FRITZ_TLS': 'false',

    # the office app to configure
    'OFFICE_CLIENT_ID': '',
    'OFFICE_CLIENT_SECRET': '',

    # The calendar to query
    'CALENDAR_NAME': 'Heizen',

    # Subject that will cause all heaters to heat for the given event time
    'CALENDAR_HEAT_ALL_SUBJECT': 'Heizen',

    # The comfort and low temperature
    'HEATING_COMFORT_TEMP': 21,
    'HEATING_LOW_TEMP': 16,

    # To reset changes made directly at the thermostat or via app
    'HEATING_AUTO_RESET': 'true',
    'HEATING_AUTO_RESET_TIME': '00:00'
}

# set this to CONFIG_NODOCKER if you are not using docker or dont want to store things in env vars
CONFIG = CONFIG_DOCKER

