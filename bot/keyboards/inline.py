from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.db_connection import Database


db = Database('bot/database/db')


async def types_keyboard(message: types.Message):
    builder = InlineKeyboardBuilder()

    types_of_sport = await db.get_types()
    for kind in types_of_sport:
        builder.button(text=kind, callback_data=kind)
    builder.adjust(1)
    await message.answer(
        text="Выбери вид спорта",
        reply_markup=builder.as_markup()
    )


async def choose_keyboard(call: types.CallbackQuery):
    global prev
    builder = InlineKeyboardBuilder()
    callback = call.data
    if call.data in await db.get_types():
        prev = callback
        leagues = await db.get_leagues(callback)
        for league in leagues:
            builder.button(text=league, callback_data=league)
        builder.adjust(1)
        await call.message.edit_text(
            text=f"Ты выбрал {callback}. Теперь выбери лигу",
            reply_markup=builder.as_markup()
        )
    else:
        teams = await db.get_teams(callback)
        for team in teams:
            builder.button(text=team, callback_data=team)
        builder.adjust(1)
        if callback in await db.get_teams(prev):
            await db.set_favourite_team(user_id=call.from_user.id, favourite_team=call.data)
            await call.message.edit_text(text="Я запомнил твою любимую команду!:)")
        else:
            await call.message.edit_text(
                text=f"Ты выбрал {callback}. Теперь выбери команду",
                reply_markup=builder.as_markup()
            )
    prev = call.data

