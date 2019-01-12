# python-fritz-office-365-sync settings

CONFIG = {
    # fritzbox
    # Only hostname or ip. No http or www
    'FRITZ_IP': 'fritz.box',
    'FRITZ_USER': 'fritzctl',
    'FRITZ_PW': 'mypw',

    # the office app to configure
    'OFFICE_CLIENT_ID': '',
    'OFFICE_CLIENT_SECRET': '',

    # The calendar to query
    'CALENDAR_NAME': 'Heizen',

    # Subject that will cause all heaters to heat for the given event time
    'CALENDAR_HEAT_ALL_SUBJECT': 'Heizen'
}

