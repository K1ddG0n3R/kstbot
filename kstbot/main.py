import asyncio
import sys
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode

import config
from handlers import router

bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


async def main() -> None:
    if not config.BOT_TOKEN:
        logging.critical("No token provided")
        sys.exit(1)

    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
