# python-fritz-office-365-sync settings

CONFIG = {
    # Only hostname or ip. No http or www
    'FRITZ_IP': 'fritz.box',
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

