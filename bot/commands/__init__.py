__all__ = ['register_user_commands', 'bot_commands', 'parsing']

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.filters import Text

from bot.commands.parsing import validation
from bot.commands.start import start
from bot.commands.keyboard_menu import sport_keyboard, set_football_team, set_hockey_team, call_edit_sport
from bot.commands.get_info import get_date

bot_commands = (
    ("start", "Нажми, чтобы начать", "Команда, которая начнет диалог и вывыедет навигацию по боту"),
    ("help", "Нажми, если возникли проблемы", "Команда, подсказывающая пользователю, что делать в случае проблем"),
    ("edit_team", "Нажми, чтобы выбрать любимую команду", "Устанавливает новую команду"),
    ("get_date", "Нажми, чтобы получить дату игры для команды", "Получает дату игры для команды"),
)


# Тут будем регистрировать команды пользователя и подключать нужные функции
def register_user_commands(router: Router) -> None:
    router.message.register(start, Command(commands=['start']))
    router.message.register(sport_keyboard, Command(commands=['edit_team']))
    router.message.register(get_date, Command(commands=['get_date']))


def menu_inline(router: Router) -> None:
    router.callback_query.register(set_football_team, F.data == "football")
    router.callback_query.register(set_hockey_team, F.data == "hockey")
