import os
import time

import requests
import schedule
from aiogram import types

from database.db_connection import Database
from parsing.parsing import send_date_of_match


async def last_match() -> None:
    db = Database()
    club, team_tag = db.get_tag(message.from_user.id)
    try:
        await message.answer(send_date_of_match(club, team_tag))
    except:
        await message.answer('К сожалению, на ближайшие дни матчей нет. Если появятся, то я тебе сообщу ;)')
