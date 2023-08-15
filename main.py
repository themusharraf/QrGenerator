import os
import pyqrcode as qr
from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TOKEN') # token
import png
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_send(msg: types.Message):
    await msg.answer("Salom link yoki qr qilmoqchi bulgan so'z yuboring 🤖")

@dp.message_handler()
async def send_qr(msg: types.Message):
    await msg.answer("Tayyorlanmoqda 👽")
    qrr = qr.create(msg.text)
    qrr.png('qrcreator.png', scale=6)

    with open('qrcreator.png', 'rb') as image:
        await bot.send_photo(msg.chat.id, image,)
        await bot.send_message(msg.chat.id, "Tayyor 👋")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
