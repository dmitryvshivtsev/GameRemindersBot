import enum
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from callback_data_states import MyCallbackData
from database.db_queries import Database

db = Database()


class Status(enum.Enum):
    add_team = 'add_team'
    selected_type = 'selected_type'
    selected_league = 'selected_league'
    selected_team = 'selected_team'
    del_team = 'del_team'


async def main_menu(message: types.Message) -> None:
    """Send the main menu"""
    builder = InlineKeyboardBuilder()
    builder.button(text="Добавить команду", callback_data=MyCallbackData(cb="add_team",
                                                                         status=Status.add_team.value).pack())
    builder.button(text="Удалить команду", callback_data=MyCallbackData(cb="del_team",
                                                                        status=Status.del_team.value).pack())
    builder.adjust(1)
    await message.answer(
        text="Что ты хочешь сделать?",
        reply_markup=builder.as_markup()
    )


async def select_kind_of_sport(query: types.CallbackQuery) -> None:
    """Replaces keyboard and show all kinds of sport"""
    builder = InlineKeyboardBuilder()
    types_of_sport = await db.get_all_types()
    for kind in types_of_sport:
        builder.button(text=kind, callback_data=MyCallbackData(cb=kind, status=Status.selected_type.value).pack())
    builder.adjust(1)
    await query.message.edit_text(
        text=f"Выбери вид спорта 🏅",
        reply_markup=builder.as_markup()
    )


async def select_league(query: types.CallbackQuery, callback_data: MyCallbackData) -> None:
    """Replaces keyboard and show all leagues"""
    builder = InlineKeyboardBuilder()
    leagues = await db.get_all_leagues(kind=callback_data.cb)
    for league in leagues:
        builder.button(text=league, callback_data=MyCallbackData(cb=league, status=Status.selected_league.value).pack())
    builder.adjust(1)
    await query.message.edit_text(
        text=f"Ты выбрал {callback_data.cb.lower()}. Теперь выбери лигу ⬇️",
        reply_markup=builder.as_markup()
    )


async def select_team(query: types.CallbackQuery, callback_data: MyCallbackData) -> None:
    """Replaces keyboard and show all teams in league"""
    builder = InlineKeyboardBuilder()
    teams = await db.get_all_teams(league=callback_data.cb)
    for team in teams:
        builder.button(text=team, callback_data=MyCallbackData(cb=team, status=Status.selected_team.value).pack())
    builder.adjust(1)
    await query.message.edit_text(
        text=f"Ты выбрал {callback_data.cb}. Теперь выбери команду ⬇️",
        reply_markup=builder.as_markup()
    )


async def set_team(query: types.CallbackQuery, callback_data: MyCallbackData) -> None:
    """Writes to database user's favourite team"""
    await db.set_favourite_team(tg_id=query.from_user.id, favourite_team=callback_data.cb)
    await query.message.edit_text(text=f"Ты болеешь за {callback_data.cb}. Круто! 😍\nЯ это запомнил и буду тебя "
                                          f"уведомлять о предстоящих матчах ежедневно в 9:00 и 21:00 🕘\n"
                                          f"А когда матч закончится, я сообщу тебе счёт 🔊")


async def del_team_keyboard(query: types.CallbackQuery) -> None:
    await query.message.edit_text(text="Удаление команд пока в разработке")

