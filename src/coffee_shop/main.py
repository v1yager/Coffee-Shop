import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from coffee_shop.bot.handlers import router
from coffee_shop.bot.config import settings
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode



dp = Dispatcher()
dp.include_router(router)

async def main() -> None:
    bot = Bot(token=settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())