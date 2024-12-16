from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


import app.keyboards as kb
from app.middlewares import TestMiddeware


router = Router()

router.message.outer_middleware(TestMiddeware())



class Register(StatesGroup):
    name = State()
    grade= State()
    number = State()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f"Привет! \nтвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}",
                        reply_markup= kb.main)


@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer("Мне самому нужно помощь")


# @router.message(Command('schedule'))
# async def schedule(message: Message):
#     await message.answer("Расписание пока в разработке", reply_markup= kb.edit_schedule)


# @router.message(Command('get_photo'))
# async def get_photo(message: Message):
#     await message.answer_photo(photo= 'AgACAgIAAxkBAAMhZ13sE_d6-7XmWc5BdWoGRpzb3TgAAsPsMRsEG_FKc3Fe1s2yo4MBAAMCAAN5AAM2BA',
#                                caption= 'это твое фото')


# @router.message(F.photo)
# async def get_photo(message: Message):
#     await message.answer(F"ID фото: {message.photo[-1].file_id}")


# @router.callback_query(F.data == 'catalog')
# async def catalog(callback: CallbackQuery):
#     await callback.answer('Вы выбрали каталог')
#     await callback.message.answer('Привет!')


# @router.callback_query(F.data == 'basket')
# async def basket(callback: CallbackQuery):
#     await callback.answer('Вы выбрали корзину', show_alert= True)
#     await callback.message.answer('Корзина')


# @router.callback_query(F.data == 'cars')
# async def cars(callback: CallbackQuery):
#     await callback.answer('Нажмите на вашу марку машины')
#     await callback.message.edit_text('Какая у тебя машина?', reply_markup= await kb.inline_cars())


# @router.message(Command('reg'))
# async def reg_first(message: Message, state: FSMContext):
#     await state.set_state(Reg.name)
#     await message.answer('Введите Ваше имя')


# @router.message(Reg.name)
# async def reg_second(message: Message, state: FSMContext):
#     await state.update_data(name = message.text)
#     await state.set_state(Reg.number)
#     await message.answer('Введите номер телефона')


# @router.message(Reg.number)
# async def two_three(message: Message, state: FSMContext):
#     await state.update_data(number = message.text)
#     data = await state.get_data()
#     await message.answer(f'Спасибо, регистрация завершена.\nИмя: {data["name"]}\nНомер: {data["number"]}')
#     await state.clear()


@router.message(F.text == 'Рассписание')
async def schedule(message: Message):
    await message.answer('Рассписание пока в разработке', reply_markup= kb.edit_schedule)


@router.callback_query(F.data == 'edit')
async def edit(callback: CallbackQuery):
    await callback.answer('Расписание пока нельзя изменить', show_alert= True)
    await callback.message.edit_text('Расписание пока в разработке')


@router.message(F.text == 'Близжайшее занятие')
async def next_lesson(message: Message):
    await message.answer('К сожалению рассписания пока нет')


@router.message(F.text == 'Дз')
async def home_work(message: Message):
    await message.answer('Данная функция в разработке')


@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ваше имя')


@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name= message.text)
    await state.set_state(Register.grade)
    await message.answer('Напишите в каком вы классе')


@router.message(Register.grade)
async def register_grade(message: Message, state: FSMContext):
    await state.update_data(grade= message.text)
    await state.set_state(Register.number)
    await message.answer('Отправьте ваш номер телефона', reply_markup= kb.get_number)


@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(number= message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Ваше имя: {data["name"]}\nВаш класс: {data["grade"]}\nНомер: {data["number"]}')
    await state.clear()
