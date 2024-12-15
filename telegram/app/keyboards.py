from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard= [
    [KeyboardButton(text = 'Каталог')],
    [KeyboardButton(text= 'Коризна'), KeyboardButton(text= 'Контакты')]
],
                            resize_keyboard= True,
                            input_field_placeholder= 'Выберете пункт меню')


settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text= 'YouTube', url= 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')],
    [InlineKeyboardButton(text= 'Каталог', callback_data= 'catalog')],
    [InlineKeyboardButton(text= 'Корзина', callback_data= 'basket')],
    [InlineKeyboardButton(text= 'Какая у тебя машина?', callback_data= 'cars'),]
    ])


cars = ['Tesla', 'Mercedes', 'BMW', 'Toyota']

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url= 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
    return keyboard.adjust(2).as_markup()