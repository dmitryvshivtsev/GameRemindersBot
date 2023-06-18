import os
import time
import requests

from aiogram import types
from database.db_queries import Database
from parsing.parsing import send_date_of_match


async def get_date(message: types.Message) -> None:
    db = Database()
    result = db.get_all_tags(message.from_user.id)
    for club, team_tag in result:
        if club and team_tag:
            try:
                await message.answer(send_date_of_match(club, team_tag))
            except:
                await message.answer(f'К сожалению, на ближайшие дни у клуба {club} нет матчей 😿\n'
                                     f'Если появятся, то я тебе сообщу 🔔')
        else:
            await message.answer('У тебя не выбрана любимая команда. Выбери её с помощью /edit_team')


def auto_get_date() -> None:
    db = Database()
    for id_ in db.get_all_tg_id():
        result = db.get_all_tags(id_)
        for club, team_tag in result:
            if club and team_tag:
                match_info = send_date_of_match(club, team_tag)
                if not match_info:
                    url = f"https://api.telegram.org/bot{os.getenv('TOKEN')}" \
                          f"/sendMessage?chat_id={id_}&" \
                          f"text='К сожалению, на ближайшие дни у клуба {club} нет матчей 😿\n" \
                          f"Если появятся, то я тебе сообщу 🔔'"
                else:
                    url = f"https://api.telegram.org/bot{os.getenv('TOKEN')}" \
                          f"/sendMessage?chat_id={id_}&" \
                          f"text={match_info}"
                requests.get(url)
                time.sleep(0.5)
