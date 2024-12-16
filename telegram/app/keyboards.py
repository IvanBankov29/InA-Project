from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from app.database.requests import get_categories, get_category_item

"""основная клавиатура"""
main = ReplyKeyboardMarkup(keyboard= [
    [KeyboardButton(text = 'Рассписание')],
    [KeyboardButton(text= 'Близжайшее занятие'), KeyboardButton(text= 'Дз')]
],
                            resize_keyboard= True,
                            input_field_placeholder= 'Выберете пункт меню')


# settings = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text= 'YouTube', url= 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')],
#     [InlineKeyboardButton(text= 'Каталог', callback_data= 'catalog')],
#     [InlineKeyboardButton(text= 'Корзина', callback_data= 'basket')],
#     [InlineKeyboardButton(text= 'Какая у тебя машина?', callback_data= 'cars'),]
#     ])


# cars = ['Tesla', 'Mercedes', 'BMW', 'Toyota']

# async def inline_cars():
#     keyboard = InlineKeyboardBuilder()
#     for car in cars:
#         keyboard.add(InlineKeyboardButton(text=car, url= 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
#     return keyboard.adjust(2).as_markup()
"""клавиатура для изменения рассписания"""
edit_schedule = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text= 'Изменить расписание', callback_data= 'edit')]
    ])

"""клавиатура для отправки номера"""
get_number = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text= 'Отправить номер', request_contact= True)]
], 
                                resize_keyboard= True,
                                input_field_placeholder= 'Дать номер телефона')


async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}"))
    keyboard.add(InlineKeyboardButton(text= 'На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def items(category_id):
    all_items = await get_category_item(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f"Item_{item.id}"))
    keyboard.add(InlineKeyboardButton(text= 'На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()
