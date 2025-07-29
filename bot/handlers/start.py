from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "Assalomu alaykum!\nYangiliklarni ko‘rish uchun /news deb yozing.\n\nCommentlar uchun /comments news_id deb yozing")
