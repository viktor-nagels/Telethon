from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
import csv

# Fill in your own API ID and hash here
api_id = 29897393
api_hash = 'dc658af18895c141e58532591ccbb239'
phone_number = '+32468114221'
chat_id = 956234626
max_messages = 120

async def main():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        entity = await client.get_entity(chat_id)
        with open('export.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['sender_user_id', 'message_text']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            async for message in client.iter_messages(entity, limit=max_messages):
                if isinstance(entity, PeerUser):
                    sender_user_id = entity.user_id
                elif isinstance(entity, PeerChat):
                    sender_user_id = message.from_id.user_id
                elif isinstance(entity, PeerChannel):
                    sender_user_id = message.sender_id.user_id
                else:
                    continue
                writer.writerow({'sender_user_id': sender_user_id, 'message_text': message.text})

if __name__ == '__main__':
    # Run the main function using the asyncio event loop
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())