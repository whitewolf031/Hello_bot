from telebot import types

def general_languange():
    keyboards = types.InlineKeyboardMarkup()
    btn_uz = types.InlineKeyboardButton(text="uz", callback_data="uz")
    btn_en = types.InlineKeyboardButton(text="en", callback_data="en")
    btn_ru = types.InlineKeyboardButton(text="ru", callback_data="ru")
    keyboards.row(btn_uz, btn_en, btn_ru)
    return keyboards

def menu_keyboards():
    keyboards = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_laptops = types.KeyboardButton(text="Noutbook")
    btn_phone = types.KeyboardButton(text="Telefon")
    btn_tv = types.KeyboardButton(text="Televizor")
    btn_back = types.KeyboardButton(text="Tilni o'zgartirish")
    keyboards.row(btn_laptops)
    keyboards.row(btn_phone)
    keyboards.row(btn_tv)
    keyboards.row(btn_back)
    return keyboards
