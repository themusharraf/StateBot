from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn = [
    [
        KeyboardButton(text="Register"), KeyboardButton(text="Login")
    ]
]
keyboard = ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True)

btnGen = [
    [KeyboardButton(text="Male"), KeyboardButton(text="Female")]
]
gen = ReplyKeyboardMarkup(keyboard=btnGen, resize_keyboard=True)
