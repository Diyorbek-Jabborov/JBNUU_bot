from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

callback = CallbackData('ikb', 'action')
button = InlineKeyboardMarkup(
    inline_keybord=[
        [
            InlineKeyboardButton(text="🔄 PDF ga o'girish", callback_data=callback.new(action='finish'))
        ],
        [
            InlineKeyboardButton(text="❌ Bekor qilish", callback_data=callback.new(action='cancel'))
        ]
    ]
)