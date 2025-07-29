from aiogram import Router, types
from aiogram.filters import Command
from bot.utils.db_client import get_news

router = Router()


@router.message(Command("news"))
async def news_handler(message: types.Message):
    news_list = await get_news()

    if not news_list:
        await message.answer("Yangiliklar hozircha yo‘q.")
        return

    for news in news_list:
        await message.answer(
            f"📰 <b>{news.title}</b>\n\n{news.content}",
            parse_mode="HTML"
        )
