from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import MessageMediaPhoto
from tqdm import tqdm
import csv
import os


def download_media(group, cl, name, offset_id, choice):
    messages = cl.get_messages(group, limit=3000, offset_id=offset_id)
    actions = {
        1: ((lambda m: isinstance(m.media, MessageMediaPhoto)), 'images.csv'),
        2: ((lambda m: m.video), 'videos.csv'),
        3: ((lambda m: m.file), 'files.csv')
    }
    cond, filename = actions.get(choice, (None, None))
    if not cond:
        print(f'Invalid choice {choice}.')
        return offset_id
    
    for message in tqdm(messages):
        if cond(message):
            file_path = message.download_media('./' + name + '/')
            if file_path:
                file_name = os.path.basename(file_path)
                with open(filename, 'a', newline='') as f:
                    writer = csv.writer(f, delimiter=';')
                    writer.writerow([message.id, file_name])

    return messages[-1].id if messages else offset_id


def download_all_media(chat, client, title_Download_Folder, choice):
    offset_id = 0
    while True:
        try:
            offset_id = download_media(chat, client, title_Download_Folder, offset_id, choice)
        except ValueError:
            print("All messages downloaded.")
            break
    print("DONE")


api_id = 29897393  # Your API ID
api_hash = 'dc658af18895c141e58532591ccbb239'  # Your API HASH
title_Download_Folder = 'DOWNLOADS'
# chat_name = str(input("chat name: "))
chat_name = '🔥🔞 HOOFDDOEKJES 18+ 🔥🍑'
print(" images(1) \n videos(2) \n files(3)")
choice = int(input("What do you want to export: "))

with TelegramClient('name', api_id, api_hash) as client:
    result = client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=500,
        hash=0,
    ))

    download_all_media(chat_name, client, title_Download_Folder, choice)
