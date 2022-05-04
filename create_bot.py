from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from dotenv import load_dotenv
import os


load_dotenv()
token_bot = os.getenv('TOKEN_BOT')

bot = Bot(token=token_bot)
dispatcher = Dispatcher(bot)