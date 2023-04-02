from typing import Union

from aiogram import types
from aiogram.filters import Command

from keyboards.inline import types_keyboard, league_keyboard, teams_keyboard, choose_keyboard


async def show_menu(message: types.Message):
    await types_keyboard(message)
