from aiogram import types


def travel_guide_keyboard():
    buttons = [
        [types.KeyboardButton(text='🔎 Найти фото')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard
