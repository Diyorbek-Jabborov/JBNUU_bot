from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

jbnuu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = 'Xodimlar'),
            KeyboardButton(text = "Fakultetitlar"),
        ],
        [
            KeyboardButton(text="Manzil"),
            KeyboardButton(text="Ishonch telefoni"),
        ],
        [
            KeyboardButton(text="Orqaga")

        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)