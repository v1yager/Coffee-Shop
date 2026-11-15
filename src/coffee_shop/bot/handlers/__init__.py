from aiogram import Router

from coffee_shop.bot.handlers import chat, start


router = Router()

router.include_routers(start.router, chat.router)