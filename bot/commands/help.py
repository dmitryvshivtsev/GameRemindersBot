from aiogram import types


async def help_call(message: types.Message) -> None:
    await message.answer(f'1) Чтобы узнать дату и время ближайшего матча твоей любимой, введи команду /get_date\n'
                          '2) Если хочешь изменить любимую команду, то введи команду /edit_team\n'
                          '3) Если есть пожелания или замечания, то напиши мне: @dmitryvshivtsev\n\n'
                          'Удачи! :)')
