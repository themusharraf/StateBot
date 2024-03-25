from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    name = State()
    age = State()
    gender = State()
    birthday = State()
    password = State()
    finish = State()
