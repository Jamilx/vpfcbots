from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import *
import os

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher(bot)











@dp.message_handler()
async def echo_send(message : types.Message):
    await message.answer(message.text)
    await message.reply(message.text)
    await message.bot.send_massage(message.from_user.id, "text")


executor.start_polling(dp, skip_updates = True)