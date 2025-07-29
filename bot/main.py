from aiogram import Bot, Dispatcher
from django.conf import settings
from bot.handlers import start, news, comments

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

dp.include_router(start.router)
dp.include_router(news.router)
dp.include_router(comments.router)
