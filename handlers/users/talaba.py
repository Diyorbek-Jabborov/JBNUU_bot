from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.talabakeyboard import talaba
from keyboards.default.jbnuukeyboard import jbnuu
from keyboards.default.menukeyboard import menu

from loader import dp


@dp.message_handler(text="Shaxsiy ma'lumotlar")
async def send_link(message:Message):
    await message.answer("Hemisdan shaxsiy ma'lumotlarni olish haqida", reply_markup=talaba)


@dp.message_handler(text="Parolni yangilash")
async def send_link(message:Message):
    await message.answer("Parolni yangilash haqida ma'lumot bo'ladi", reply_markup=talaba)


@dp.message_handler(text="To'lov shartnomani olish")
async def send_link(message:Message):
    await message.answer("To'lov shartnomani olish haqida ma'lumot bo'ladi", reply_markup=talaba)


@dp.message_handler(text="O'qish joyidan ma'lumotnoma olish")
async def send_link(message:Message):
    await message.answer("O'qish joyidan ma'lumot olish", reply_markup=talaba)


@dp.message_handler(text="Chaqiruv qog'ozi")
async def send_link(message:Message):
    await message.answer("Chaqiruv qog'ozini olish bo'yicha ma'lumotnoma", reply_markup=talaba)


@dp.message_handler(text="Reyting daftarcha")
async def send_link(message:Message):
    await message.answer("Reyting daftarcha bo'yicha qo'llanma", reply_markup=talaba)


@dp.message_handler(text="Orqaga")
async def send_link(message:Message):
    await message.answer("Siz orqaga qaytdingiz", reply_markup=menu)

