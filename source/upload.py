import sys
import os
from requests.packages.urllib3 import disable_warnings
from telebot import TeleBot

token = 'YOUR_BOT_TOKEN_HERE'
chat_id = 'CHAT_ID_FOR_UPLOAD_HERE'

try:
    from token import token
    from token import chat_id
except:
    pass

disable_warnings()
bot = TeleBot(token)


# https://core.telegram.org/bots/api#sending-files
# https://core.telegram.org/api/obtaining_api_id
def upload(file_name):
    print file_name,
    message = bot.send_document(chat_id, open(file_name, 'rb'))
    data = bot.get_file(message.document.file_id)
    print "-> https://api.telegram.org/file/bot{}/{}".format(bot.token, data.file_path)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: upload.py file_for_upload"
        sys.exit(1)
    else:
        upload(sys.argv[1])
