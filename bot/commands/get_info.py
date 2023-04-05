from aiogram import types
from aiogram.filters import CommandObject

from database.db_connection import Database
from parsing.parsing import send_date_of_match


async def get_date(message: types.Message) -> None:
    db = Database()
    club, team_tag =  await db.get_tag(message.from_user.id)
    try:
        await message.answer(await send_date_of_match(club, team_tag))
    except:
        await message.answer('Не найден матч :(\nУбедись, что ты уже выбрал любимую команду')
