from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import InputPeerEmpty
from tqdm import tqdm
import csv
import os
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER')

def export_user_ids(chat, client):
    # Create a CSV file to store the user IDs
    with open('user_ids.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['User ID'])

        # Get all the participants in the chat
        participants = client.iter_participants(chat, aggressive=True)

        # Write each participant's ID to the CSV file
        for participant in tqdm(participants):
            writer.writerow([participant.id])



chat_name = '🔥🔞 HOOFDDOEKJES 18+ 🔥🍑'

with TelegramClient('name', api_id, api_hash) as client:
    while True:
        try:
            export_user_ids(chat_name, client)
            break
        except Exception as e:
            print(f"Error occurred: {e}")
            continue
