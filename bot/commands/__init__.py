__all__ = ['register_user_commands', 'bot_commands', 'menu_inline']


from aiogram import Router, F
from aiogram.filters import Command

from commands.callback_data_states import MyCallbackData
from commands.get_info import get_date
from commands.help import help_call
from commands.messages import text_msg
from commands.start import start
from database.db_queries import Database
from keyboards.inline import main_menu, del_team_keyboard, select_kind_of_sport, select_league, \
    select_team, set_team, del_team, show_teams

db = Database()


bot_commands = (
    ("start", "Нажми, чтобы начать", "Команда, которая начнет диалог и вывыедет навигацию по боту"),
    ("help", "Нажми, если есть вопросы", "Команда, подсказывающая пользователю, что делать в случае проблем"),
    ("edit_team", "Нажми, чтобы выбрать любимую команду", "Устанавливает новую команду"),
    ("get_date", "Узнай когда ближайшая игра у твоей любимой команды", "Получает дату игры для команды"),
)


async def register_user_commands(router: Router) -> None:
    router.message.register(start, Command(commands=['start']))
    router.message.register(main_menu, Command(commands=['edit_team']))
    router.message.register(get_date, Command(commands=['get_date']))
    router.message.register(help_call, Command(commands=['help']))
    router.message.register(text_msg, F)


async def menu_inline(router: Router) -> None:
    router.callback_query.register(select_kind_of_sport, MyCallbackData.filter(F.status == 'add_team'))
    router.callback_query.register(select_league, MyCallbackData.filter(F.status == 'selected_type'))
    router.callback_query.register(select_team, MyCallbackData.filter(F.status == 'selected_league'))
    router.callback_query.register(set_team, MyCallbackData.filter(F.status == 'selected_team'))
    router.callback_query.register(del_team_keyboard, MyCallbackData.filter(F.status == 'del_team'))
    router.callback_query.register(del_team, MyCallbackData.filter(F.status == 'selected_del_team'))
    router.callback_query.register(show_teams, MyCallbackData.filter(F.status == 'show_user_teams'))
