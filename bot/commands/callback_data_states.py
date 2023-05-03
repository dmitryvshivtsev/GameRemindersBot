from aiogram.filters.callback_data import CallbackData


class MyCallbackData(CallbackData, prefix="my"):
    cb: str
    status: str
