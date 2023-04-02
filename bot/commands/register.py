from aiogram import types
from database import db_connection


db = db_connection.Database('bot/database/db')


async def registration(message: types.Message):
    if not (db.user_exists(message.from_user.id)):
        await message.answer(f'Мы запомнили твое имя :)\nТеперь нужно узнать твой любимый вид спорта и команду.')
        db.add_user(message.from_user.id, message.from_user.username)
    else:
        await message.answer('Вы уже зарегистрированы! :)')
