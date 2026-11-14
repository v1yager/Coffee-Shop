from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()

@router.message(Command("start"))
async def start_handler(message: Message) -> None:
    await message.answer(f"Hello, {message.from_user.username}")