from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.talabakeyboard import talaba
from keyboards.default.jbnuukeyboard import jbnuu
from keyboards.default.menukeyboard import menu

from loader import dp


@dp.message_handler(text="Shaxsiy ma'lumotlar")
async def send_link(message:Message):
    shaxsiy = open('Resource/hemis-shaxsiy-malumotlar.pdf', 'rb')
    await message.answer_document(document=shaxsiy,
                                  caption="Talabaning shaxsiy ma'lumotlari!!!\n"
                                          "                   \n"
                                          "✅ Hemis tizimining TALABA PROFILI talabaning o'ziga tegishli shaxsiy "
                                          "ma'lumotlarini ko'rish imkoniyatini beradi \n"
                                          "                        \n"
                                          "Agar shaxsiy ma'lumotlarizda xatolik bo'lsa adminga murojaat qiling, javob berilmagan "
                                          "holda dekanatga murojaat qiling!!!",
                                  reply_markup=talaba)


@dp.message_handler(text="Parolni yangilash")
async def send_link(message:Message):
    parol = open('Resource/Parolni_tiklash_instruksiyasi.pdf', 'rb')
    await message.answer_document(document=parol,
                                  caption="🔢 Hemis tizimida talabaning parolini tiklash!!! \n"
                                          "                   \n"
                                          "✅ Parolni tiklash uchun PIN kod orqali talabaning haqiqiyligi tekshiriladi va "
                                          "uning profilidagi elektron pochta manziliga va telefon raqamiga PIN koddan iborat xabar"
                                          "yuboriladi. SMS xabar pullik (40 so'm), talabaning xisobidan olinadi. \n"
                                          "                     \n"
                                          "❓ Funksiyadan foydalanish uchun talabaning profiliga elektron pochta yoki telefon raqami"
                                          "kiritilgan bo'lishi shart. \n"
                                          "                 \n"
                                          "Ushbu faylda funksiyadan foydalanish yo'riqnomasi keltirilgan.",
                                  reply_markup=talaba)


@dp.message_handler(text="To'lov shartnomani olish")
async def send_link(message:Message):
    shartnoma = open('Resource/hemis-shartnoma.pdf', 'rb')
    await message.answer_document(document=shartnoma,
                                  caption="🔢 Hemis tizimida talabaning to'lov shartnoma olish!!! \n"
                                          "                \n"
                                          "✅ To'lov shartnomani kontrakt.edu.uz elektron platforma orqali olinadi "
                                          "(shartnomaga buyurtma berishdan oldin shaxsiy ma'lumotlaringizni tekshirishni "
                                          "unutmang). To'lov-shartnoma summasini shartnomada ko'rsatilgan vaqtda to'lash talab "
                                          "etiladi. Shartnoma shartlari bajarilmagan holda tuzilgan shartnoma bekor bo'lishi mukin.",
                                  reply_markup=talaba)



@dp.message_handler(text="O'qish joyidan ma'lumotnoma olish")
async def send_link(message:Message):
    malumotnoma = open('Resource/hemis-malumotnoma.pdf', 'rb')
    await message.answer_document(document=malumotnoma,
                                  caption="🔢 Hemis tizimida talabaning o'qish joyidan ma'lumotnoma olish!!! \n"
                                          "    \n"
                                          "Ma'lumotnoma QR-KoD bilan pdf formatda taqdim etiladi. \n"
                                          "    \n"
                                          "✅ Talaba o'z kabinetida Ma'lumotnomalar bo'limida Ma'lumotnoma olish knopkasi "
                                          "bosish orqali joriy semestr uchun ma'lumotnoma shakllantiradi. Shundan so'ng"
                                          "faylni yuklab olish belgisiga bosgan xolga yuklab oladi. \n"
                                          "    \n"
                                          "❗️ Talabada bitta semestr uchun bir marta ma'lumotnoma olish imkoniyati mavjud.",
                                  reply_markup=talaba)


@dp.message_handler(text="Chaqiruv qog'ozi")
async def send_link(message:Message):
    chaqiruv = open('Resource/hemis-chaqiruv-qog-ozi.pdf', 'rb')
    await message.answer_document(document=chaqiruv,
                                  caption="🔢 Hemis tizimida chaqiruv qog'ozi olish!!! \n"
                                          "     \n"
                                          "✅ Hemis tizida chaqiruv qog'ozi o'qish vaqti boshlanganda ish joyidan ruxsat olish uchun"
                                          "kerak bo'ladigan hujjat. \n"
                                          "     \n"
                                          "⁉️ Agarda hemis tizimida chaqiruv qog'ozi ko'rinmasa Sirtqi (maxsus sirtqi) bo'limi xodimlariga "
                                          "murojaat qilishingizni so'raymiz.",
                                  reply_markup=talaba)


@dp.message_handler(text="Reyting daftarcha")
async def send_link(message:Message):
    reyting = open('resource/hemis-reyting-daftarcha.pdf', 'rb')
    await message.answer_document(document=reyting,
                                  caption="🔢 Hemis tizimida talaba reyting daftarchasi!!! \n"
                                          "    \n"
                                          "✅ Hemis tizida ma'lumotlaringiz tog'ri ekanligini tekshiring agar ma'lumotlaringizda"
                                          "xatolik aniqlansa adminga yoki dekanatga murojaat qiling.",
                                  reply_markup=talaba)


@dp.message_handler(text="Orqaga")
async def send_link(message:Message):
    await message.answer("Siz orqaga qaytdingiz", reply_markup=menu)

