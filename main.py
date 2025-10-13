from telebot import TeleBot
# from keyboards import *
import random

token = "7595867257:AAHVZaPpWl4Tss_CITtWX3a67BBrpBjuBx0"

bot = TeleBot(token)
number = random.randint(1, 10)

@bot.message_handler(commands="start")
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Raqamni toping")
    bot.register_next_step_handler(message, find_number)

def find_number(message):
    chat_id = message.chat.id
    raqam = message.text

    if number == int(raqam):
        bot.send_message(chat_id, "Topdingiz")

    if number != int(raqam):
        bot.send_message(chat_id, "Noto'g'ri. Qayta raqam kiriting")
        bot.register_next_step_handler(message, find_number)
    
bot.polling(none_stop=True)
