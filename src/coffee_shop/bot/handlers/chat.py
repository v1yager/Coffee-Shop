from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from coffee_shop.bot.services.openai_service import generate_response
 

router = Router()

@router.message(F.text)
async def chat_handler(message: Message) -> None:
    response = await generate_response(message.from_user.id, message.text)
    await message.answer(response)