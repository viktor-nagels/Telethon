from telethon.sync import TelegramClient
import customtkinter
import tkinter
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import MessageMediaPhoto
from dotenv import load_dotenv
from tqdm import tqdm
import csv
import os

load_dotenv()


api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER')
title_Download_Folder = 'DOWNLOADS'
# chat_name = str(input("chat name: "))
# chat_name = '🔥🔞 HOOFDDOEKJES 18+ 🔥🍑'
# chat_name = 956234626
print("images(1)")
print("videos(2)")
print("files(3)")
choice = int(input("What do you want to export: "))



def download_media(group, cl, name, offset_id):
    messages = cl.get_messages(group, limit=3000, offset_id=offset_id)

    for message in tqdm(messages):
        if choice == 1 and isinstance(message.media, MessageMediaPhoto):
            file_path = message.download_media('./' + name + '/')
            if file_path:
                file_name = os.path.basename(file_path)
                with open('images.csv', 'a', newline='') as f:
                    writer = csv.writer(f, delimiter=';')
                    writer.writerow([message.id, file_name])
        elif choice == 2 and message.video:
            file_path = message.download_media('./' + name + '/')
            if file_path:
                file_name = os.path.basename(file_path)
                with open('videos.csv', 'a', newline='') as f:
                    writer = csv.writer(f, delimiter=';')
                    writer.writerow([message.id, file_name])
        elif choice == 3 and message.file:
            file_path = message.download_media('./' + name + '/')
            if file_path:
                file_name = os.path.basename(file_path)
                with open('files.csv', 'a', newline='') as f:
                    writer = csv.writer(f, delimiter=';')
                    writer.writerow([message.id, file_name])

    return messages[-1].id if messages else offset_id

def download_all_media(chat, client, title_Download_Folder):
    offset_id = 0
    while True:
        try:
            offset_id = download_media(chat, client, title_Download_Folder, offset_id)
        except ValueError:
            print("All messages downloaded.")
            break
    print("DONE")

with TelegramClient('name', api_id, api_hash) as client:
    result = client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=500,
        hash=0,
    ))

    download_all_media(chat_name, client, title_Download_Folder)
