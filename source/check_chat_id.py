from requests.packages.urllib3 import disable_warnings
from telebot import TeleBot

token = 'YOUR_BOT_TOKEN_HERE'
try:
    from token import token
except:
    pass

disable_warnings()
bot = TeleBot(token)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print "## message from chat ID:", message.chat.id
    bot.reply_to(message, 'message.chat.id: %s' % message.chat.id)


bot.polling()
