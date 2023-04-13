import os
import time

import requests
import schedule
from aiogram import types

from database.db_connection import Database
from parsing.parsing import send_date_of_match


async def last_match() -> None:
    db = Database()
    pass