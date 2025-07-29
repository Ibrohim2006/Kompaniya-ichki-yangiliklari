import json, asyncio
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from aiogram import Bot
from aiogram.types import Update
from django.conf import settings

from bot.main import dp

bot = Bot(token=settings.BOT_TOKEN)


@csrf_exempt
def telegram_webhook(request):
    if request.method == "POST":
        update = Update.model_validate(json.loads(request.body))
        asyncio.create_task(dp.feed_update(bot, update))
        return JsonResponse({"status": "ok"})
    return JsonResponse({"error": "invalid method"}, status=405)
