from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f"Привет! \nтвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}",
                        reply_markup= kb.main)



@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer("Это команда /help")



@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer("ОК!")



@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo= 'AgACAgIAAxkBAAMhZ13sE_d6-7XmWc5BdWoGRpzb3TgAAsPsMRsEG_FKc3Fe1s2yo4MBAAMCAAN5AAM2BA',
                               caption= 'это твое фото')



@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(F"ID фото: {message.photo[-1].file_id}")