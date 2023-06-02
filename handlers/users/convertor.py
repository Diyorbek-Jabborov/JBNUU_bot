# from aiogram import types
# from aiogram.dispatcher.filters import Command, Text
# from aiogram.types import Message, ReplyKeyboardRemove
# from keyboards.default.menukeyboard import menu
# from keyboards.inline.myButton import callback, button
#
#
# from loader import dp
#
# # @dp.message_handler(text="Rasmni pdf qilish")
# # async def send_link(message:Message):
# #     await message.answer("Rasmni pdf qilish")
#
#
# @dp.message_handler(content_types=types.ContentType.PHOTO)
# async def get_photo(message:types.Message):
#     await message.reply(text=f"✅ <b>Rasm qabul qilindi!</b>\n\n"
#                              f"➕ <b>Agar davom etmoqchi bo'lsangiz yana rasm yuklang...</b>\n\n"
#                              f"<b>Yoki....\n</b>"
#                              f"👇🏻<b>Kerakli buyruqni tanlang...</b>", reply_markup=button)

import asyncio
import os
from aiogram import Bot, types
from fpdf import FPDF

async def convert_image_to_pdf(image_path, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(image_path, x=10, y=10, w=190)
    pdf.output(output_path, "F")

async def send_pdf_to_user(bot, chat_id, pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        await bot.send_document(chat_id, pdf_file)

bot_token = 'YOUR_BOT_TOKEN'
bot = Bot(token=bot_token)

@bot.message_handler(content_types=types.ContentType.PHOTO)
async def handle_photo(message: types.Message):
    photo = message.photo[-1]
    image_path = f"photo_{photo.file_id}.jpg"
    await photo.download(image_path)
    pdf_path = f"photo_{photo.file_id}.pdf"
    await convert_image_to_pdf(image_path, pdf_path)
    await send_pdf_to_user(bot, message.chat.id, pdf_path)
    os.remove(image_path)
    os.remove(pdf_path)
