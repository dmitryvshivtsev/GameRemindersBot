from aiogram import types


async def help_call(message: types.Message) -> None:
    await message.answer(f'1) Чтобы узнать информацию о ближайшем матче, введи команду `/get_date эвертон` (например)\n'
                         '2) Если есть пожелания или замечания, то напиши мне: @dmitryvshivtsev\n\n'
                         'Удачи! :)')