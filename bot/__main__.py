import os
import asyncio
import logging
from asyncio import create_task

from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand
from commands import register_user_commands, bot_commands, menu_inline
from database.db_connection import Database


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))

    dp = Dispatcher()
    bot = Bot(token=os.getenv('TOKEN'))

    set_commands = create_task(bot.set_my_commands(commands=commands_for_bot))
    # await bot.set_my_commands(commands=commands_for_bot)
    db = Database()

    await set_commands

    menu = create_task(menu_inline(dp))

    start_poll = dp.start_polling(bot)

    register_user_commands(dp)
    # await menu_inline(dp)
    # await dp.start_polling(bot)

    await menu
    await start_poll


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
