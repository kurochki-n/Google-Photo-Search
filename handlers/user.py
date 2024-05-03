from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from . import localization as loc, keyboards as kb
from .states_menu import Form
from google.search_engine import run_searching


router = Router()


@router.message(Command("start"))
async def start(message: Message, state: FSMContext) -> None:
    await message.answer(text=loc.start_message(message.from_user.first_name), reply_markup=kb.travel_guide_keyboard())
    await state.set_state(Form.none_state)


@router.message(F.text == "🔎 Найти фото")
async def get_description(message: Message, state: FSMContext) -> None:
    await message.answer(text=loc.get_description(), reply_markup=kb.travel_guide_keyboard())
    await state.set_state(Form.wait_description)
    
    
@router.message(StateFilter(Form.wait_description))
async def photo_search(message: Message, state: FSMContext) -> None:
    await message.answer(text=loc.photo_search(), reply_markup=kb.travel_guide_keyboard())
    await run_searching(message)
    await state.set_state(Form.none_state)
    

    








