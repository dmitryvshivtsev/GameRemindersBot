from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.db_connection import Database

db = Database()


async def main_menu(message: types.Message) -> None:
    builder = InlineKeyboardBuilder()
    builder.button(text="Добавить команду", callback_data="add_team")
    builder.button(text="Удалить команду", callback_data="del_team")
    builder.adjust(1)
    await message.answer(
        text="Что ты хочешь сделать?",
        reply_markup=builder.as_markup()
    )


async def edit_team_keyboard(call: types.CallbackQuery) -> None:
    global prev
    builder = InlineKeyboardBuilder()
    callback = call.data
    if call.data == "add_team":
        types_of_sport = await db.get_all_types()
        for kind in types_of_sport:
            builder.button(text=kind, callback_data=kind)
        builder.adjust(1)
        await call.message.edit_text(
            text=f"Выбери вид спорта 🏅",
            reply_markup=builder.as_markup()
        )
    elif call.data in await db.get_all_types():
        prev = callback
        leagues = await db.get_all_leagues(kind=callback)
        for league in leagues:
            builder.button(text=league, callback_data=league)
        builder.adjust(1)
        await call.message.edit_text(
            text=f"Ты выбрал {callback.lower()}. Теперь выбери лигу ⬇",
            reply_markup=builder.as_markup()
        )
    else:
        teams = await db.get_all_teams(callback)
        for team in teams:
            builder.button(text=team, callback_data=team)
        builder.adjust(1)
        if callback in await db.get_all_teams(prev):
            await db.set_favourite_team(tg_id=call.from_user.id, favourite_team=call.data)
            await call.message.edit_text(text=f"Ты болеешь за {callback}. Круто! 😍\nЯ это запомнил и буду тебя "
                                              f"уведомлять о предстоящих матчах ежедневно в 9:00 и 21:00 🕘\n"
                                              f"А когда матч закончится, я сообщу тебе счёт 🔊")
        else:
            await call.message.edit_text(
                text=f"Ты выбрал {callback}. Теперь выбери команду ⬇",
                reply_markup=builder.as_markup()
            )
    prev = call.data

