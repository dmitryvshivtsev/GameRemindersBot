from aiogram import types

from database.db_queries import Database


async def test(message: types.Message) -> None:
    db = Database()
    fav_team = await db.get_arr(message.from_user.id)
    if fav_team:
        await message.answer(f"Твои любимые команды: {fav_team[0]}")
    else:
        await message.answer(f"У тебя нет любимой команды :(\nВыбери её с помощью /edit_team")
