from aiogram import Router, types
from aiogram.filters import Command
from bot.utils.db_client import get_news

router = Router()


@router.message(Command("news"))
async def news_handler(message: types.Message):
    news_list = await get_news()

    if not news_list:
        await message.answer("📰 Hozircha yangiliklar mavjud emas.")
        return

    for idx, news in enumerate(news_list, start=1):
        text = (
            f"📰 <b>{news.title}</b>\n"
            f"📅 <i>{news.created_at.strftime('%d.%m.%Y')}</i>\n\n"
            f"{news.content[:200]}..."
        )
        await message.answer(
            text,
            parse_mode="HTML",
        )
