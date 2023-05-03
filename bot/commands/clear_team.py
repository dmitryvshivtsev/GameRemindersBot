from aiogram import types
from database.db_queries import Database


async def clear_team(message: types.Message) -> None:
    db = Database()
    db.clear_favourite_team(tg_id=message.from_user.id)
    await message.answer("Я очистил любимую команду!\nТы всегда можешь выбрать новую с помощью /edit_team :)")
