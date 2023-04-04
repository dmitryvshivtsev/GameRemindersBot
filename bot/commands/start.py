import os

from aiogram import types

from database.db_connection import Database


async def start(message: types.Message) -> None:
    db = Database()

    await message.answer(f'Привет, {message.chat.first_name}! Добро пожаловать в бота, который не позволит тебе пропустить игру любимой'
                         ' команды!'
                         '\n\n1) Если есть проблемы, введи команду /help\n'
                         '2) Чтобы узнать информацию о ближайшем матче, введи команду `/get_date название_команды`\n\n'
                         'Удачи! :)')
    if not (db.user_exists(message.from_user.id)):
        await message.answer(f'Мы запомнили твое имя :)\nТеперь нужно узнать твой любимый вид спорта и команду. Для этого вызови команду /edit_team')
        db.add_user(message.from_user.id, message.from_user.username)
