__all__ = ['register_user_commands', 'bot_commands']

import sqlite3

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.filters import Text

from database.db_connection import Database
# from bot.commands.parsing import validation
from start import start
from menu.inline_menu import show_menu
from menu.inline_menu import league_keyboard, teams_keyboard, types_keyboard, choose_keyboard
from get_info import get_date
from register import registration
from register import bot_msg
from help import help_call



bot_commands = (
    ("start", "Нажми, чтобы начать", "Команда, которая начнет диалог и вывыедет навигацию по боту"),
    ("help", "Нажми, если возникли проблемы", "Команда, подсказывающая пользователю, что делать в случае проблем"),
    ("edit_team", "Нажми, чтобы выбрать любимую команду", "Устанавливает новую команду"),
    ("reg", "Нажми для регистрации, если ты тут впервые"),
    ("get_date", "Через пробел укажи название команды (на русском), чтобы получить дату игры", "Получает дату игры для команды"),
)


# Тут будем регистрировать команды пользователя и подключать нужные функции
def register_user_commands(router: Router) -> None:
    router.message.register(start, Command(commands=['start']))
    router.message.register(types_keyboard, Command(commands=['edit_team']))
    router.message.register(get_date, Command(commands=['get_date']))
    router.message.register(registration, Command(commands=['reg']))
    router.message.register(help_call, Command(commands=['help']))
    router.message.register(bot_msg, F)


db = Database('bot/database/db')


async def menu_inline(router: Router) -> None:
    router.callback_query.register(choose_keyboard)
