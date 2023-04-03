from aiogram import types

from database.db_connection import Database
from keyboards.inline import types_keyboard, choose_keyboard


async def show_menu(message: types.Message):
    db = Database('bot/database/db')
    if not (db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id, message.from_user.username)
    await types_keyboard(message)
