# **python-fritz-office-365-sync**  - Office365 to Fritzbox Sync

# Setup 

### Setup Cron

The script needs to be scheduled. Best way to do this is to add a cron-job which fires the script every 5 minutes. 

```
*/5  *    * * *   pyFritz    /srv/python-fritz-office-365-sync/script.py
```

### Setup Office365 App

You should set os variables: `OFFICE_CLIENT_ID` and  `OFFICE_CLIENT_SECRET`. To get `OFFICE_CLIENT_ID` and `OFFICE_CLIENT_SECRET`  you should follow the steps:

1. Login to <https://apps.dev.microsoft.com/>

2. Create an app, note your `OFFICE_CLIENT_ID`

3. Generate a new password (`OFFICE_CLIENT_SECRET`) under `Application Secrets` section

4. Under the `Platform` section, add a new web platform and set `http://localhost:5000` as the redirect URL

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