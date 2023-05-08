from telethon import TelegramClient, events
import csv
import datetime
import os
from dotenv import load_dotenv

load_dotenv()


#* VARIABLES 
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER')
subfolder_name = input('Enter the name of the subfolder to save the files in: ')


#* GENERATE SUBFOLDER IF NOT EXISTS
if not os.path.exists(subfolder_name):
    os.makedirs(subfolder_name)

#* GENERATE CLIENT OBJECT
client = TelegramClient('session_name', api_id, api_hash)

#* server connection
client.start(phone_number)

#* Create log file and 2 csv files
log_file = open(f'{subfolder_name}/log_file.txt', 'a', encoding='utf-8')


csv_file_path = f'{subfolder_name}/user_id_displayed_name.csv'
csv_file_exists = os.path.exists(csv_file_path)
csv_file = open(csv_file_path, 'a', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)

csv_file_path1 = f'{subfolder_name}/chat_id_displayed_name.csv'
csv_file_exists1 = os.path.exists(csv_file_path1)
csv_file1 = open(csv_file_path1, 'a', newline='', encoding='utf-8')
csv_writer1 = csv.writer(csv_file1)


#* CHECK if exists
if csv_file_exists:
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        user_id_displayed_name = {row[0]: row[1] for row in csv_reader}
else:
    user_id_displayed_name = {}

if csv_file_exists1:
    with open(csv_file_path1, 'r', encoding='utf-8') as csv_file1:
        csv_reader1 = csv.reader(csv_file1)
        chat_id_displayed_name = {row[0]: row[1] for row in csv_reader1}
else:
    chat_id_displayed_name = {}

# Define a function to handle incoming messages
@client.on(events.NewMessage())
async def handle_message(event):
    # Get the time the message was sent
    time_sent = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Get the channel ID and name the message was sent in
    channel_id = event.chat_id
    chat = await event.get_chat()
    channel_name = chat.title

    # Get the user ID and displayed name of the message sender
    user_id = event.sender_id
    user = await event.get_sender()
    displayed_name = user.first_name + " " + user.last_name if user.last_name else user.first_name

    # Write the message information to the log file
    log_file.write(f'{time_sent}, {str(channel_id)[1:]}, {user_id}, {displayed_name}, {event.text}\n')

    # Add the user ID and displayed name to the user_id_displayed_name dictionary if it doesn't already exist
    if user_id not in user_id_displayed_name and displayed_name:
        user_id_displayed_name[user_id] = displayed_name
        csv_writer.writerow([user_id, displayed_name])

    # Add the channel ID and name to the chat_id_displayed_name dictionary if it doesn't already exist
    if channel_id not in chat_id_displayed_name and channel_name:
        chat_id_displayed_name[channel_id] = channel_name
        csv_writer1.writerow([str(channel_id)[1:], channel_name])

# Start the client and run it until it is stopped
print('(Press Ctrl+C to stop this)')
client.run_until_disconnected()

# Close the log file and CSV file
log_file.close()
csv_file.close()
