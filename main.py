from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from config import *
from function import *
from asyncio import run

dp = Dispatcher()

async def startAdminAnswer(bot: Bot):
    await bot.send_message(chat_id=admin_id, text="Bot Ready")

async def botShutdownAnswer(bot: Bot):
    await bot.send_message(chat_id=admin_id, text="Bot off")
    
async def start():
    dp.startup.register(startAdminAnswer)
    dp.shutdown.register(botShutdownAnswer)
    dp.message.register(startAnswer, CommandStart())
    
    bot = Bot(token=bot_token)
    await dp.start_polling(bot, polling_timeout=1)
    
run(start())