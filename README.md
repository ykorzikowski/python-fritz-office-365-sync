# Office365 to Fritzbox Thermostat Sync

# Setup 

Currently the token refreshment is not working properly. See https://github.com/O365/python-o365/issues/167

Also you have to manually compile https://github.com/ykorzikowski/fritzbox-smarthome until the author has accepted my pull request https://github.com/DerMitch/fritzbox-smarthome/issues/20

### Compile Fritzhome

```
git clone https://github.com/ykorzikowski/fritzbox-smarthome.git
cd fritzbox-smarthome
python3 setup.py sdist bdist_wheelpython3 setup.py sdist bdist_wheel
cp /dist/fritzhome-1.0.6.tar.gz /tmp
```

### Setup PyEnv

```
git clone https://github.com/ykorzikowski/python-fritz-office-365-sync
pyenv install 3.7.0
cd python-fritz-office-365-sync
sudo apt-get install python3.5-venv
./venv3.5/bin/pip3 install /tmp/fritzhome-1.0.6.tar.gz
./venv3.5/bin/pip install -r requirements.txt

```

### Setup Cron

The script needs to be scheduled. Best way to do this is to add a cron-job which fires the script every 5 minutes. 

```
*/5  *    * * *   fritzsync    /srv/python-fritz-office-365-sync/venv3.5/bin/python -m python-fritz-office-365-sync.core
```

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

If you want to access the fritzbox from the internet, you have to set up the myFritz! access first. After this, you have to copy the self-signed certificate from your browser to `conf/fritz.crt` and set `FRITZ_TLS`property to true. 

Disable the heating time tables by setting the temperature to 16° for all days & times. 

### Setup the calendar

Add a new calendar with the outlook account you used to run this script. You need to add the name of the calendar in the config. 

# Usage

Create new appointments in the calendar to add heating periods. As subject, use the wildcard, which will heat up all thermostats or specify the name of the thermostat. 

## Used Librarys

https://github.com/zopyx/python-office365-calendar

https://github.com/DerMitch/fritzbox-smarthome
