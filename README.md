# Telegram Auto Reply Bot
A Telegram script That will Reply private messages on telegram with a fixed message.
Check the [Telethon](https://telethon.readthedocs.io/en/latest/index.html) documentation.

### How does it work?
You only need to get the api_id and the api_hash from the [Telegram Core](https://my.telegram.org/auth?to=apps).
After you create your new app, you'll have access to these items.

```
# your phone number must start with country code
phone = 'YOUR PHONE NUMBER'
# use your username like this ✔yourusername not like this ❌@yourusername 
username = 'YOUR USERNAME'
# if you have two-step verification enabled put your password here
# or if you don't have it remove the line or put hash(#) infront of it
# like this #password = 'YOUR PASSWORD'
password = 'YOUR PASSWORD' 

# content of the automatic reply
message = "Hello There!\n\nSorry I am currently Busy." \
          "\nYour message will be responded when I am free, Thanks"
```

### Install Packages
```
pip install -r requirements.txt
```
### Run The Script
```
python bot.py
```
