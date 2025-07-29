import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from aiogram.types import Update
from bot.main import bot, dp
import logging

logger = logging.getLogger(__name__)


@csrf_exempt
async def telegram_webhook(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            update = Update.model_validate(data)

            await dp.feed_update(bot, update)

            return JsonResponse({"status": "ok"})

        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON: {e}")
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

        except Exception as e:
            logger.error(f"Error processing update: {e}", exc_info=True)
            return JsonResponse({"error": "Internal server error"}, status=500)

    return JsonResponse({"error": "Method not allowed"}, status=405)
