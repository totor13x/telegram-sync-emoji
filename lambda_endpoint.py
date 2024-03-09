

from dotenv import load_dotenv
load_dotenv('.env')

import json
import os

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import functions, types

api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
acc_token = os.environ.get('ACC_TOKEN')
lambda_token = os.environ.get('LAMBDA_TOKEN')

statuses = {
    "default": 5841403144604487992,
    "work": 5246772116543512028,
    "snooze": 5247100325059370738,
    "hidden": 5839434146912407382,
    "dota": 5404333301034927124
}


def lambda_handler(event, context):
    try:
        if (event["queryStringParameters"]["token"] == lambda_token):
            set_status = "default"
            if "status" in event["queryStringParameters"]:
                set_status = event["queryStringParameters"]["status"]
            
            if set_status not in statuses:
                return {"error": "Invalid status"}, 400

            with TelegramClient(StringSession(acc_token), api_id, api_hash) as client:
                result = client(functions.account.UpdateEmojiStatusRequest(
                    emoji_status=types.EmojiStatus(
                        document_id=statuses[set_status]
                    )
                ))
        
                return {"result": result and "ok" or "fail"}
        else:
            return "none"
    except BaseException:
        return "not handled"

if __name__ == "__main__":
    lambda_handler({"queryStringParameters": {"token": lambda_token,"status": "default"}}, {})