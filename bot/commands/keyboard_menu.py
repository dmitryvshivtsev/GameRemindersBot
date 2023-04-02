from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton
# from bot.parsing.parsing import validation


async def sport_keyboard(message: types.Message) -> None:
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup()

    # kinds_of_sport = await get_sport()
    # for sport in kinds_of_sport:

    builder = InlineKeyboardBuilder()
    builder.button(
        text="Футбол",
        callback_data="football"
    )
    builder.button(
        text="Баскетбол",
        callback_data="basketball"
    )
    builder.button(
        text="Хоккей",
        callback_data="hockey"
    )
    builder.adjust(1)
    await message.answer(
        "Выбери вид спорта",
        reply_markup=builder.as_markup()
    )


async def team_keyboard(sport):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup()

    # teams = await get_teams()
    # for team in teams:


async def set_football_team(call: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(
        text="PSG",
        callback_data="psg"
    )
    builder.button(
        text="Everton",
        callback_data="everton"
    )
    builder.adjust(1)
    await call.message.edit_reply_markup(
        "Выбери команду",
        reply_markup=builder.as_markup()
    )


async def set_hockey_team(call: types.CallbackQuery) -> None:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Ак Барс",
        callback_data="ak-bars"
    )
    builder.button(
        text="ЦСКА",
        callback_data="cska-hockey"
    )
    builder.adjust(1)
    await call.message.answer(
        "Выбери команду",
        reply_markup=builder.as_markup()
    )


async def call_edit_sport(call: types.CallbackQuery):
    return await call.message.edit_reply_markup()