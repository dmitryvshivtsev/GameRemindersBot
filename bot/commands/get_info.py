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
        await message.answer('Не найден матч :(\nУбедись, что ты уже выбрал любимую команду')


# @schedule.repeat(schedule.every(10).seconds)
def auto_get_date() -> None:
    db = Database()
    for id_ in db.get_tg_id():
        club, team_tag = db.get_tag(id_)
        try:
            url = f"https://api.telegram.org/bot{os.getenv('TOKEN')}/sendMessage?chat_id={id_}&text={send_date_of_match(club, team_tag)}"
        except:
            url = f"https://api.telegram.org/bot{os.getenv('TOKEN')}/sendMessage?chat_id={id_}&text={'Что-то не так'}"
        requests.get(url)
        time.sleep(1)


async def notificate() -> None:
    schedule.every(1).minute.do(auto_get_date())
