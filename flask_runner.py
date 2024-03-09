from flask import Flask, request
from dotenv import load_dotenv
import os
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import functions, types
import nest_asyncio
 
 
load_dotenv('.env')
 
app = Flask(__name__)
nest_asyncio.apply()
 
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
acc_token = os.getenv('ACC_TOKEN')
 
statuses = {
    "default": 5841403144604487992,
    "work": 5246772116543512028,
    "snooze": 5247100325059370738,
    "hidden": 5839434146912407382,
    "dota": 5404333301034927124
}
 
@app.route('/set_status', methods=['GET'])
def set_status():
    try:
        set_status = request.args.get('status', default="default")
 
        if set_status not in statuses:
            return {"error": "Invalid status"}, 400
 
        with TelegramClient(StringSession(acc_token), api_id, api_hash) as client:
            result = client(functions.account.UpdateEmojiStatusRequest(
                emoji_status=types.EmojiStatus(
                    document_id=statuses[set_status]
                )
            ))
    
            return {"result": result and "ok" or "fail"}
    except BaseException:
        return {"error": "not handled"}, 500
 
if __name__ == "__main__":
    app.run(debug=True)