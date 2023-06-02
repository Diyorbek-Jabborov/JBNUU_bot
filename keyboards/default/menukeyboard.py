from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="JBNUU haqida"),
            KeyboardButton(text='Hemis platformasi '),
        ],
        [
            KeyboardButton(text="Biz bilan bog'lanish"),
            KeyboardButton(text="Rasmni pdf qilish")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)