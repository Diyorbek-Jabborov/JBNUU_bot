from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.talabakeyboard import talaba
from keyboards.default.jbnuukeyboard import jbnuu
from keyboards.default.menukeyboard import menu

from loader import dp


@dp.message_handler(text="Xodimlar")
async def send_link(message:Message):
    await message.answer("Xodimlar haqida ma'lumot bo'ladi", reply_markup=jbnuu)


@dp.message_handler(text="Fakultetitlar")
async def send_link(message: Message):
    await message.answer("Fakultetitlar haqida ma'lumot bo'ladi", reply_markup=jbnuu)


@dp.message_handler(text="Manzil")
async def send_link(message: Message):
    await message.answer("Manzil haqida ma'lumot bo'ladi", reply_markup=jbnuu)


@dp.message_handler(text="Ishonch telefoni")
async def send_link(message: Message):
    await message.answer("Ishonch telefoni boladi", reply_markup=jbnuu)


@dp.message_handler(text="Orqaga")
async def send_link(message: Message):
    await message.answer("Orgaga qaytdingiz", reply_markup=menu)

