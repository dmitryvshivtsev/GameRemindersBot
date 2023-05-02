__all__ = ['register_user_commands', 'bot_commands', 'menu_inline']


from aiogram import Router, F
from aiogram.filters import Command

from callback_data_states import MyCallbackData
from commands.get_info import get_date
from commands.messages import text_msg
from commands.help import help_call
from commands.start import start
from commands.favourite_team import favourite_team
from commands.clear_team import clear_team
from keyboards.inline import main_menu, select_team_keyboard, del_team_keyboard
from database.db_connection import Database

db = Database()


bot_commands = (
    ("start", "Нажми, чтобы начать", "Команда, которая начнет диалог и вывыедет навигацию по боту"),
    ("help", "Нажми, если есть вопросы", "Команда, подсказывающая пользователю, что делать в случае проблем"),
    ("edit_team", "Нажми, чтобы выбрать любимую команду", "Устанавливает новую команду"),
    ("get_date", "Узнай когда ближайшая игра у твоей любимой команды", "Получает дату игры для команды"),
    ("clear_team", "Нажми, чтобы я забыл про твою любимую команду", "Очищает в БД любимую команду для пользователя"),
    ("favourite_team", "Нажми, если забыл, какая команда выбрана твоей любимой", "Возвращает пользователю его любимую команду")
)


async def register_user_commands(router: Router) -> None:
    router.message.register(start, Command(commands=['start']))
    router.message.register(main_menu, Command(commands=['edit_team']))
    router.message.register(favourite_team, Command(commands=['favourite_team']))
    router.message.register(get_date, Command(commands=['get_date']))
    router.message.register(help_call, Command(commands=['help']))
    router.message.register(clear_team, Command(commands=['clear_team']))
    router.message.register(text_msg, F)


async def menu_inline(router: Router) -> None:
    router.callback_query.register(select_team_keyboard, MyCallbackData.filter())
