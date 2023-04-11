import os
import time

import requests
import schedule
from aiogram import types

from database.db_connection import Database
from parsing.parsing import send_date_of_match


async def get_date(message: types.Message) -> None:
    db = Database()
    club, team_tag = db.get_tag(message.from_user.id)
    try:
        await message.answer(send_date_of_match(club, team_tag))
    except:
        await message.answer('К сожалению, на ближайшие дни матчей нет. Если появятся, то я тебе сообщу ;)')


# @schedule.repeat(schedule.every(10).seconds)
def auto_get_date() -> None:
    db = Database()
    for id_ in db.get_tg_id():
        club, team_tag = db.get_tag(id_)
        try:
            url = f"https://api.telegram.org/bot{os.getenv('TOKEN')}" \
                  f"/sendMessage?chat_id={id_}&" \
                  f"text={send_date_of_match(club, team_tag)}"
        except:
            url = f"https://api.telegram.org/bot{os.getenv('TOKEN')}" \
                  f"/sendMessage?chat_id={id_}&" \
                  f"text={'К сожалению, на ближайшие дни матчей нет. Если появятся, то я тебе сообщу ;)'}"
        requests.get(url)
        time.sleep(1)
