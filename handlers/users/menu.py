from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.talabakeyboard import talaba
from keyboards.default.jbnuukeyboard import jbnuu
from keyboards.default.menukeyboard import menu
from loader import dp


@dp.message_handler(text="Hemis platformasi")
async def send_link(message:Message):
    await message.answer("Hemis tizimi haqida qo'llanma", reply_markup=talaba)


@dp.message_handler(text="JBNUU haqida")
async def send_link(message: Message):
    await message.answer("JBNUU haqida: ", reply_markup=jbnuu)


@dp.message_handler(text="Biz bilan bog'lanish")
async def send_link(message:Message):
    await message.answer("Biz bilan bog'lanishingiz mumkin", reply_markup=menu)

