from aiogram.filters.callback_data import CallbackData


class MyCallbackData(CallbackData, prefix="test"):
    cb: str
    status: int
