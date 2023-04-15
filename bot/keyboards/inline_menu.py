import asyncio
import os

from aiogram import types

from database.db_connection import Database
from keyboards.inline import types_keyboard, choose_keyboard


async def show_menu(message: types.Message) -> None:
    db = Database()
    exist = asyncio.create_task(db.user_exists(tg_id=message.from_user.id))
    if not (await exist):
        db.add_user(tg_id=message.from_user.id, tg_username=message.from_user.username)
    await types_keyboard(message)
