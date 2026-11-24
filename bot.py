from telegram.ext import Updater, MessageHandler, Filters

BOT_TOKEN = "9129539104:AAHm42hIe43jyP72c3zRyzbA4uGc_YW9ups"
SECRET_KEY = "Lucky proxy"

def check_key(update, context):
    user_text = update.message.text.strip()
    if user_text.lower() == SECRET_KEY.lower():
        update.message.reply_text("VALID")
    else:
        update.message.reply_text("INVALID")

updater = Updater(BOT_TOKEN)
updater.dispatcher.add_handler(MessageHandler(Filters.text, check_key))
updater.start_polling()
updater.idle()
