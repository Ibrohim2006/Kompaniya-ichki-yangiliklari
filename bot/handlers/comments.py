from aiogram import Router, types
from aiogram.filters import Command
from bot.utils.db_client import get_comments

router = Router()


@router.message(Command("comments"))
async def comments_handler(message: types.Message):
    args = message.text.split()

    if len(args) < 2:
        await message.answer("❗ Foydalanish: <b>/comments news_id</b>", parse_mode="HTML")
        return

    news_id = args[1]

    if not news_id.isdigit():
        await message.answer("❗ News ID raqam bo‘lishi kerak!")
        return

    comments = await get_comments(int(news_id))

    if not comments:
        await message.answer("💬 Bu yangilikda hali izohlar yo‘q.")
        return

    text = f"💬 <b>News ID: {news_id}</b> izohlari:\n\n"
    for comment in comments:
        text += f"👤 <b>{comment.user.email}</b>\n"
        text += f"✍️ {comment.message}\n"
        text += f"📅 {comment.created_at.strftime('%Y-%m-%d %H:%M')}\n\n"

    await message.answer(text, parse_mode="HTML")
