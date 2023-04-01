from aiogram import types
from aiogram.filters import Command


async def show_menu(message: types.Message):
    await list_types_of_sport(message)


async def list_types_of_sport(message: [types.Message, types.CallbackQuery], **kwargs):
    markup = await types_keyboard()
