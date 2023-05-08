from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest, GetHistoryRequest
from telethon.tl.types import InputPeerEmpty
from tqdm import tqdm
import csv
import os
from dotenv import load_dotenv

load_dotenv()


api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER')
chat_name = '🔥🍑SEX ON THE BEACH PRIVE CLUB🔥🍑'
user_id = 5120940718

def export_messages(client, chat, user_id):
    offset_id = 0
    limit = 100
    all_messages = []

    while True:
        messages = client(GetHistoryRequest(
            peer=chat,
            offset_id=offset_id,
            offset_date=None,
            add_offset=0,
            limit=limit,
            max_id=0,
            min_id=0,
            hash=0
        ))

        if not messages.messages:
            break

        for message in messages.messages:
            if message.from_id.user_id == user_id:
                all_messages.append((message.id, message.date, message.message))

        offset_id = messages.messages[-1].id

    with open('BERICHTEN.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Message ID', 'Sent Timestamp', 'Message Text'])
        for message in all_messages:
            writer.writerow([message[0], message[1], message[2]])

    print(f"{len(all_messages)} messages exported to BERICHTEN.csv")

with TelegramClient('name', api_id, api_hash) as client:
    # Get the dialogs
    result = client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=500,
        hash=0,
    ))

    # Find the chat with the specified name
    for chat in result.chats:
        if chat.title == chat_name:
            target_chat = chat
            break

    # Export all messages sent by the specified user in the target chat
    export_messages(client, target_chat, user_id)
