from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


def travel_guide_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text='🔎 Найти фото')]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard
