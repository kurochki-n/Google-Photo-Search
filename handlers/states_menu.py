from aiogram.filters.state import State, StatesGroup

class Form(StatesGroup):
    wait_description = State()
    none_state = State()