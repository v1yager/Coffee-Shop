import asyncio

from aiogram import F, Router
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.types import Message

from coffee_shop.bot.services.openai_service import generate_response
 

router = Router()

async def keep_typing(message: Message) -> None:
    while True:
        await message.bot.send_chat_action(
            chat_id=message.chat.id,
            action=ChatAction.TYPING
        )
        await asyncio.sleep(4)

@router.message(F.text)
async def chat_handler(message: Message) -> None:
    typing_task = asyncio.create_task(keep_typing(message))

    try:
        response = await generate_response(message.from_user.id, message.text)
        await message.answer(response)
    finally:
        typing_task.cancel()