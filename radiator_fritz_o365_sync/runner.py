import time
import logging
from conf.conf import CONFIG as conf
from radiator_fritz_o365_sync.core import Core

if __name__ == "__main__":
    if conf['DEBUG_LOGGING']:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    logging.info("started radiator_fritz_o365_sync runner")
    while True:
        logging.info("syncing with office calendar...")
        Core().run()
        time.sleep(conf['POLLING_INTERVAL'])
