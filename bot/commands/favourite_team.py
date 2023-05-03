from aiogram import types

from database.db_queries import Database


async def favourite_team(message: types.Message) -> None:
    db = Database()
    fav_team = await db.get_favourite_team(message.from_user.id)
    if fav_team:
        await message.answer(f"Твоя любимая команда: {fav_team}")
    else:
        await message.answer(f"У тебя нет любимой команды :(\nВыбери её с помощью /edit_team")
