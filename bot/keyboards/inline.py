import enum
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
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
    builder.button(text="Добавить команду", callback_data="add_team")
    builder.button(text="Удалить команду", callback_data="del_team")
    builder.adjust(1)
    await message.answer(
        text="Что ты хочешь сделать?",
        reply_markup=builder.as_markup()
    )


status = None


async def select_team_keyboard(call: types.CallbackQuery) -> None:
    global status
    builder = InlineKeyboardBuilder()
    if call.data == "add_team":
        status = Status.add_team.value
    if status == Status.add_team.value:
        await select_kind_of_sport(call, builder)
        status = Status.selected_type.value
    elif status == Status.selected_type.value:
        await select_league(call, builder)
        status = Status.selected_league.value
    elif status == Status.selected_league.value:
        await select_team(call, builder)
        status = Status.selected_team.value
    elif status == Status.selected_team.value:
        await db.set_favourite_team(tg_id=call.from_user.id, favourite_team=call.data)
        await call.message.edit_text(text=f"Ты болеешь за {call.data}. Круто! 😍\nЯ это запомнил и буду тебя "
                                          f"уведомлять о предстоящих матчах ежедневно в 9:00 и 21:00 🕘\n"
                                          f"А когда матч закончится, я сообщу тебе счёт 🔊")
        status = Status.empty.value


async def select_kind_of_sport(call: types.CallbackQuery, builder: InlineKeyboardBuilder):
    types_of_sport = await db.get_all_types()
    for kind in types_of_sport:
        builder.button(text=kind, callback_data=kind)
    builder.adjust(1)
    await call.message.edit_text(
        text=f"Выбери вид спорта 🏅",
        reply_markup=builder.as_markup()
    )


async def select_league(call: types.CallbackQuery, builder: InlineKeyboardBuilder):
    leagues = await db.get_all_leagues(kind=call.data)
    for league in leagues:
        builder.button(text=league, callback_data=league)
    builder.adjust(1)
    await call.message.edit_text(
        text=f"Ты выбрал {call.data.lower()}. Теперь выбери лигу ⬇",
        reply_markup=builder.as_markup()
    )


async def select_team(call: types.CallbackQuery, builder: InlineKeyboardBuilder):
    teams = await db.get_all_teams(call.data)
    for team in teams:
        builder.button(text=team, callback_data=team)
    builder.adjust(1)
    await call.message.edit_text(
        text=f"Ты выбрал {call.data}. Теперь выбери команду ⬇",
        reply_markup=builder.as_markup()
    )


async def del_team_keyboard(call: types.CallbackQuery) -> None:
    await call.message.edit_text(text="Удаление команд пока в разработке")

