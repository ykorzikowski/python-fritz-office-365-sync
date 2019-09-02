# Office365 to Fritzbox Thermostat Sync

This little tool gives you the opportunity to control your radiators by your calendar. 

First you need to buy some DECT compatible thermometers for your radiators and connect them to your fritzbox. 

You can either heat all radiators up by a specified subject or create an event for each radiator by using the name of the thermostat. 

## Using Docker

```yaml
---
version: '3'

services:
  radiator-fritz-o365-sync:
    container_name: radiator_fritz_o365_sync
    image: ykorzikowski/radiator-fritz-o365:latest
    restart: always
    environment:
      TZ=Europe/Amsterdam
      FRITZ_IP=fritz.box
      FRITZ_USER=fritzctl
      FRITZ_PW=myPW
      FRITZ_TLS=false
      OFFICE_CLIENT_ID=
      OFFICE_CLIENT_SECRET=
      CALENDAR_NAME=Heating
      CALENDAR_HEAT_ALL_SUBJECT=HeatAll
    volumes:
    - '/srv/docker/volumes/radiator-o365/o365_token.txt:/usr/src/app/o365_token.txt'
    #- '/srv/docker/volumes/radiator-o365/fritz.crt:/usr/src/app/conf/fritz.crt'
```

Easiest way to set up is using docker in combination with docker-compose. See **Setup O365 & Fritzbox** for more instructions. 

After you set up your fritzbox and your o365 client secrets, you have to generate a token file via the following command: 

```bash
docker run -i -e OFFICE_CLIENT_ID='' -e OFFICE_CLIENT_SECRET='' ykorzikowski/radiator-fritz-o365 python -mradiator_fritz_o365_sync.gen_token
```

This will print out a json which has to be stored as presented in docker-compose.yml. 



## Variables Explained

`TZ` : sets the timezone

`FRITZ_IP`: the ip of the fritzbox

`FRITZ_USER`: the username to log in to fritz box

`FRITZ_PW`: password to login to fritz box

`OFFICE_CLIENT_ID`: the client id to access o365 API

`OFFICE_CLIENT_SECRET`: the secret to access o365 API

`CALENDAR_NAME`: the calendar name to query for heating items

`CALENDAR_HEAT_ALL_SUBJECT`: if calendar event is named like this, all radiators will start heating

`HEATING_COMFORT_TEMP`: default to `21`C°. the target temperature all radiators will set to

`HEATING_LOW_TEMP`: default to `16`°C. the target temperature all radiators will set to when heating is disabled

`HEATING_AUTO_RESET`: default `true`. will check radiators temperature at given time and reset them to default. this is useful when the temperature is changed directly on the radiator by a user

`HEATING_AUTO_RESET_TIME`: default to `00:00`. time when the radiator temperature will be reseted

`POLLING_INTERVALL`: default to `60` seconds - time when the calendar gets polled. 

`DEBUG_LOGGING`: default to `false` - will increase logging output 

# Manual Setup 

You have to manually compile https://github.com/ykorzikowski/fritzbox-smarthome until the author has accepted my pull request https://github.com/DerMitch/fritzbox-smarthome/issues/20

### Compile Fritzhome

```
git clone https://github.com/ykorzikowski/fritzbox-smarthome.git
cd fritzbox-smarthome
python3 setup.py sdist bdist_wheel
cp /dist/fritzhome-1.0.6.tar.gz /tmp
```

### Setup PyEnv

```
sudo apt-get install python3.5-venv
git clone https://github.com/ykorzikowski/python-fritz-office-365-sync
cd python-fritz-office-365-sync
pyvenv-3.5 ./venv3.5
./venv3.5/bin/pip3 install /tmp/fritzhome-1.0.6.tar.gz
./venv3.5/bin/pip install -r requirements.txt

```

### Setup Cron

The script needs to be scheduled. Best way to do this is to add a cron-job which fires the script every 5 minutes. 

```
*/5  *    * * *   fritzsync    /srv/python-fritz-office-365-sync/venv3.5/bin/python -m radiator_fritz_o365_sync.core
```

## Setup O365 & Fritzbox

### Setup Office365 App

You should set os variables: `OFFICE_CLIENT_ID` and  `OFFICE_CLIENT_SECRET`. To get `OFFICE_CLIENT_ID` and `OFFICE_CLIENT_SECRET`  you should follow the steps:

1. Login to <https://apps.dev.microsoft.com/>

2. Create an app, note your `OFFICE_CLIENT_ID`

3. Generate a new password (`OFFICE_CLIENT_SECRET`) under `Application Secrets` section

4. Under the `Platform` section, add a new web platform and set `https://outlook.office365.com/owa/` as the redirect URL

5. Under `Microsoft Graph Permissions` section, add the below delegated permissions:

   - User.Read

   - Files.ReadWrite

   - Calendars.Read

   - Mail.Send

### Setup Fritzbox

If you want to access the fritzbox from the internet, you have to set up the myFritz! access first. After this, you have to copy the self-signed certificate from your browser to `conf/fritz.crt` and set `FRITZ_TLS`property to true. When using docker you have to specify the file via volume. 

Disable the heating time tables by setting the temperature to 16° for all days & times. 

### Setup the calendar

Add a new calendar with the outlook account you used to run this script. You need to add the name of the calendar in the config. 

# Usage

Create new appointments in the calendar to add heating periods. As subject, use the string you specified in `CALENDAR_HEAT_ALL_SUBJECT`, which will heat up all thermostats or specify the name of the thermostat. 

## Used Librarys

https://github.com/zopyx/python-office365-calendar

https://github.com/DerMitch/fritzbox-smarthome
