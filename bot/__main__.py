import os
import asyncio
import logging
import schedule
import time
import threading

from asyncio import create_task
from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand
from commands import register_user_commands, bot_commands, menu_inline
from commands.get_info import auto_get_date
from database.db_queries import Database

import os
from dotenv import load_dotenv
from pathlib import Path


async def main() -> None:
    load_dotenv()
    logging.basicConfig(level=logging.DEBUG)

    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))

    dp = Dispatcher()
    bot = Bot(token=os.getenv('TOKEN'))

    set_commands = create_task(bot.set_my_commands(commands=commands_for_bot))
    db = Database()

    await set_commands

    menu = create_task(menu_inline(dp))
    start_poll = create_task(dp.start_polling(bot))
    user_commands = create_task(register_user_commands(dp))

    await user_commands
    await menu
    await start_poll


def schedulers_checker() -> None:
    while True:
        schedule.run_pending()
        time.sleep(0.5)


if __name__ == "__main__":
    try:
        schedule.every().day.at("09:00").do(auto_get_date)
        schedule.every().day.at("21:00").do(auto_get_date)
        threading.Thread(target=schedulers_checker).start()
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')

