from aiogram import types
from dispatcher import dp
import config

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await dp.answer("hello")