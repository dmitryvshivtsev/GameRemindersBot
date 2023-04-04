import os

from aiogram import types

from database.db_connection import Database
from keyboards.inline import types_keyboard, choose_keyboard


async def show_menu(message: types.Message):
    db = Database()
    if not (db.user_exists(tg_id=message.from_user.id)):
        db.add_user(tg_id=message.from_user.id, tg_username=message.from_user.username)
    await types_keyboard(message)
