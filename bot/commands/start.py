import asyncio
import os

from aiogram import types
from database.db_queries import Database


async def start(message: types.Message) -> None:
    db = Database()
    exist = asyncio.create_task(db.user_exists(tg_id=message.from_user.id))

    await message.answer(f'Привет, {message.chat.first_name}! Добро пожаловать в бота, который не позволит тебе пропустить игру любимой'
                         ' команды! \n\n'
                         '1) Если есть проблемы, введи команду /help 💫\n'
                         '2) Если хочешь изменить любимый вид спорта, лигу и клуб, то введи команду /edit_team 📝\n'
                         '3) Чтобы узнать информацию о ближайшем матче, введи команду /get_date 📅\n\n'
                         'Удачи! :)')
    if not (await exist):
        await message.answer(f'Мне нужно узнать твой любимый вид спорта и команду. Для этого вызови команду /edit_team')
        db.add_user(message.from_user.id, message.from_user.username)
