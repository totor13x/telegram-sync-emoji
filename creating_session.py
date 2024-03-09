import os
 
from dotenv import load_dotenv
 
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
 
load_dotenv('.env')
 
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
 
with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())