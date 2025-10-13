from telebot import TeleBot
from keyboards import *

token = "7595867257:AAHVZaPpWl4Tss_CITtWX3a67BBrpBjuBx0"
# key = "406c553c497446c099c12940102f423f"

bot = TeleBot(token)

@bot.message_handler(commands="start")
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Assalomu aleykum", reply_markup=general_languange())

@bot.callback_query_handler(func=lambda call: True)
def menu_languange(call):
    chat_id = call.message.chat.id
    if call.data == "uz":
        bot.send_message(chat_id, "Siz uzbek tilini tanladingiz", reply_markup=menu_keyboards())
        bot.register_next_step_handler(call.message, general_menu)

    if call.data == "en":
        bot.send_message(chat_id, "Siz uzbek tilini tanladingiz", reply_markup=menu_keyboards())
        bot.register_next_step_handler(call.message, general_menu)

    if call.data == "en":
        bot.send_message(chat_id, "Siz uzbek tilini tanladingiz", reply_markup=menu_keyboards())
        bot.register_next_step_handler(call.message, general_menu)

def general_menu(message):
    chat_id = message.chat.id
    if message.text == "Noutbook":
        bot.send_message(chat_id, "Noutbook")
    
    if message.text == "Telefon":
        bot.send_message(chat_id, "Telefon")

    if message.text == "Televizor":
        bot.send_message(chat_id, "Televizor")

    if message.text == "Tilni o'zgartirish":
        bot.send_message(chat_id, "Tilni tanlang", reply_markup=general_languange())

# telefon location ni aniqlash
# def contact_info(message):
#     chat_id = message.chat.id
#     phone_number = message.text
#     phoneNumbers = phonenumbers.parse(phone_number)
#     timeZone = timezone.time_zones_for_number(phoneNumbers)
#     service = carrier.name_for_number(phoneNumbers, "en")
#     geolocation = geocoder.description_for_number(phoneNumbers, "en")
#     geocoder = OpenCageGeocode(key)
#     query = str(geolocation)
#     result = geocoder.geocode(query)
#     lat = result[0]["geometry"]["let"]
#     lang = result[0]["geometry"]["lan"]
#     print(lat, lang)
#     print("location: " + geolocation)
#     print("timezone: ", timeZone)
#     print("company name: " + service)

bot.polling(none_stop=True)