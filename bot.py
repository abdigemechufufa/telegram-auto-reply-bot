import asyncio
import time
from telethon import events
from telethon.sync import TelegramClient
from telethon import functions, types

# your phone number must start with country code
phone = 'YOUR PHONE NUMBER'
# use your username like this ✔yourusername not like this ❌@yourusername 
username = 'YOUR USERNAME'
# if you have two-step verification enabled put your password here
# or if you don't have it remove the line or put hash(#) infront of it
# like this #password = 'YOUR PASSWORD'
password = 'YOUR PASSWORD' 

# content of the automatic reply
message = "Hello There!\nSorry I am currently Offline." \
          "\nYour message will be responded when I am free, Thanks"

def main():

    # Create the client and connect
    # use sequential_updates=True to respond to messages one at a time
    client = TelegramClient(username, api_id, api_hash, sequential_updates=True)

    #===========================================================================================#
    # whenever someone says "Hi" to you, it will respond your message(Hi)
    @client.on(events.NewMessage(incoming=True, pattern='(?i)hi$', func=lambda e: e.is_private))
    async def _(event):
        sender = await event.get_sender()
        first_name = sender.first_name
        await event.respond('Hi')

    #===========================================================================================#
    # send respond with first name
    @client.on(events.NewMessage(incoming=True, pattern='(?i)hi$', func=lambda e: e.is_private))
    async def _(event):
        sender = await event.get_sender()
        first_name = sender.first_name
        await event.respond('Hi %s'%first_name)

    #===========================================================================================#
    # Respond whenever someone says "Hi" and something else
    @client.on(events.NewMessage(incoming=True, pattern='(?i)hi.+', func=lambda e: e.is_private))
    async def _(event):
        await event.respond(message)

    #===========================================================================================#
    print(time.asctime(), '-', 'Auto Replying is Started')
    client.start(phone, password)
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Auto Replying is Stopped!')
    #===========================================================================================#

if __name__ == '__main__':
    main()