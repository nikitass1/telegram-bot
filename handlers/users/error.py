from aiogram import types
from loader import dp

@dp.message_handler()
async def command_start(message: types.Message):
    await message.answer(f'Комманда {message.text} неизвестна!')
