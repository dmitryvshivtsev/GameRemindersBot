from aiogram import Router, F,  types


async def text_msg(message: types.Message):
    await message.answer("Я не понимаю, что ты мне пишешь :(\n"
                         "Если у тебя есть вопросы, то вызови /help")