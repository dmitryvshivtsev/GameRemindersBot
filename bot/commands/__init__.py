__all__ = ['register_user_commands', 'bot_commands']

from aiogram import Router
from aiogram.filters import Command

from database.db_connection import Database
from get_info import get_date
# from register import bot_msg
from help import help_call
from menu.inline_menu import types_keyboard, choose_keyboard
from start import start

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
    router.message.register(help_call, Command(commands=['help']))
    # router.message.register(bot_msg, F)


db = Database('bot/database/db')


async def menu_inline(router: Router) -> None:
    router.callback_query.register(choose_keyboard)
