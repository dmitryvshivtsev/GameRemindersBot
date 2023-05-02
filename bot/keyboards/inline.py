import enum
from aiogram import types
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

from callback_data_states import MyCallbackData
from database.db_connection import Database

db = Database()


class Status(enum.Enum):
    add_team = 0
    selected_type = 1
    selected_league = 2
    selected_team = 3
    empty = None


async def main_menu(message: types.Message) -> None:
    builder = InlineKeyboardBuilder()
    builder.button(text="Добавить команду", callback_data=MyCallbackData(cb="add_team",
                                                                         status=Status.add_team.value))
    builder.button(text="Удалить команду", callback_data="del_team")
    builder.adjust(1)
    await message.answer(
        text="Что ты хочешь сделать?",
        reply_markup=builder.as_markup()
    )


# status = None
prev = None


async def select_team_keyboard(call: types.CallbackQuery, callback_data: MyCallbackData) -> None:
    # global status
    global prev
    if not prev:
        prev = callback_data
    builder = InlineKeyboardBuilder()
    if callback_data.status == Status.add_team.value:
        await select_kind_of_sport(call, builder)
    elif callback_data.status == Status.selected_type.value:
        await select_league(call, builder, prev, callback_data)
    elif callback_data.status == Status.selected_league.value:
        await select_team(call, builder, prev, callback_data)
    elif callback_data.status == Status.selected_team.value:
        await db.set_favourite_team(tg_id=call.from_user.id, favourite_team=callback_data.cb)
        await call.message.edit_text(text=f"Ты болеешь за {callback_data.cb}. Круто! 😍\nЯ это запомнил и буду тебя "
                                          f"уведомлять о предстоящих матчах ежедневно в 9:00 и 21:00 🕘\n"
                                          f"А когда матч закончится, я сообщу тебе счёт 🔊")
    prev = callback_data


async def select_kind_of_sport(call: types.CallbackQuery, builder: InlineKeyboardBuilder):
    types_of_sport = await db.get_all_types()
    for kind in types_of_sport:
        builder.button(text=kind, callback_data=MyCallbackData(cb=kind, status=Status.selected_type.value))
    builder.adjust(1)
    await call.message.edit_text(
        text=f"Выбери вид спорта 🏅",
        reply_markup=builder.as_markup()
    )


async def select_league(call: types.CallbackQuery, builder: InlineKeyboardBuilder, prev: MyCallbackData, cb: MyCallbackData):
    leagues = await db.get_all_leagues(kind=cb.cb)
    for league in leagues:
        builder.button(text=league, callback_data=MyCallbackData(cb=league, status=Status.selected_league.value))
    builder.button(text="Назад ⬅️", callback_data=MyCallbackData(cb=prev.cb, status=prev.status))
    builder.adjust(1)
    await call.message.edit_text(
        text=f"Ты выбрал {cb.cb.lower()}. Теперь выбери лигу ⬇️",
        reply_markup=builder.as_markup()
    )


async def select_team(call: types.CallbackQuery, builder: InlineKeyboardBuilder, prev: MyCallbackData, cb: MyCallbackData):
    teams = await db.get_all_teams(league=cb.cb)
    for team in teams:
        builder.button(text=team, callback_data=MyCallbackData(cb=team, status=Status.selected_team.value))
    builder.button(text="Назад ⬅️", callback_data=MyCallbackData(cb=prev.cb, status=prev.status))
    builder.adjust(1)
    await call.message.edit_text(
        text=f"Ты выбрал {cb.cb}. Теперь выбери команду ⬇️",
        reply_markup=builder.as_markup()
    )


async def del_team_keyboard(call: types.CallbackQuery) -> None:
    await call.message.edit_text(text="Удаление команд пока в разработке")

