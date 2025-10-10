from telebot import TeleBot

token = "8297531634:AAHkiVq7EM2yrTf2TsyCUZbGzsFuP_E77RE"

bot = TeleBot(token)

@bot.message_handler(commands="start")
def start(message):
    chat_id = message.chat.id
    username = message.from_user.username
    print(username)
    print(chat_id)
    bot.send_message(chat_id, "Salom qalisan")
    bot.send_message(chat_id, f"Menda seni id bor {chat_id}")
    bot.send_message(chat_id, f"Seni username menda bor {username}")

bot.polling(none_stop=True)