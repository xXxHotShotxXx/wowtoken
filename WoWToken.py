import urllib.request
import time
from win10toast import ToastNotifier
import requests
import datetime
import tempfile

# Constants
APP_NAME = 'wowtoken'
APP_VERSION = 1.0

client = Client(ClientConfig(), refresh=True)

# Returns an update object
update = client.update_check(APP_NAME, APP_VERSION)

# Optionally you can use release channels
# Channel options are stable, beta & alpha
# Note: Patches are only created & applied on the stable channel
app_update = client.update_check(APP_NAME, APP_VERSION, channel='stable')

# Use the update object to download an update & restart the app
if app_update is not None:
    downloaded = app_update.download()
    if downloaded is True:
        app_update.extract_restart()




website = 'https://us.api.battle.net/data/wow/token/?namespace=dynamic-us&locale=en_US&access_token=jnakhmxmt8rk3xna3ewqnpdw'
response = requests.get('https://us.api.battle.net/data/wow/token/?namespace=dynamic-us&locale=en_US&access_token=jnakhmxmt8rk3xna3ewqnpdw')

def check():
    response = urllib.request.urlopen(website)
    html = response.read()
    return(html)
prevhtml = check()
while True:
    newhtml = check()
    if newhtml != prevhtml:
        response = requests.get('https://us.api.battle.net/data/wow/token/?namespace=dynamic-us&locale=en_US&access_token=jnakhmxmt8rk3xna3ewqnpdw')
        price = response.text[140:146]
        ints = int(price)
        formated = (format(ints,',d'))
        toaster = ToastNotifier()
        toaster.show_toast("WoW Token",formated,icon_path="wow.ico",duration=60,threaded=True)

        print()
        print(formated)
    prevhtml = newhtml
    time.sleep(60)
