import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message


bot = Bot(token='123')
dp = Dispatcher



@dp.massage(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет!")



async def main():
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())