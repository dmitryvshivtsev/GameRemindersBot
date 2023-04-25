from aiogram import types


async def text_msg(message: types.Message) -> None:
    await message.answer("Я не понимаю, что ты мне пишешь 🥺\n"
                         "Если у тебя есть вопросы, то вызови /help 💫")