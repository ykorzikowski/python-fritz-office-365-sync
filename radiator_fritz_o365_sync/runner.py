import time
from radiator_fritz_o365_sync.core import Core

if __name__ == "__main__":
    print("started radiator_fritz_o365_sync runner")
    while True:
        print("syncing with office calendar...")
        Core().run()
        time.sleep(60)
