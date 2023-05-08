
from telethon import TelegramClient, events, sync
api_id = 29897393
api_hash = 'dc658af18895c141e58532591ccbb239'
# username = 6187844353
username = int(input("username_id: "))


client = TelegramClient('session_name', api_id, api_hash)
client.start()

# print(client.get_me().stringify())
async def handler(update):
    print(update)




# client.send_message('username', 'Hello! Talking to you from Telethon')
# client.send_file('username', '/home/myself/Pictures/holidays.jpg')

client.download_profile_photo('me')
messages = client.get_messages(username)
messages[0].download_media()


while True:
    message = str(input("Write her your message: "))
    if message != '':
        client.send_message(username, message)
    else:
        print("no value is given")
    client.add_event_handler(handler)


