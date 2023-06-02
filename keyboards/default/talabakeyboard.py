from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

talaba = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Shaxsiy ma'lumotlar"),
            KeyboardButton(text="Parolni yangilash"),
        ],
        [
            KeyboardButton(text="To'lov shartnomani olish"),
            KeyboardButton(text="O'qish joyidan ma'lumotnoma olish"),
        ],
        [
            KeyboardButton(text="Chaqiruv qog'ozi"),
            KeyboardButton(text="Reyting daftarcha")
        ],

        [
            KeyboardButton(text="Orqaga"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)