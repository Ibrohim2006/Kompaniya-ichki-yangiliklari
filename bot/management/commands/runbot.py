# bot/management/commands/runbot.py
import asyncio, os
from django.core.management.base import BaseCommand
from django.conf import settings
from aiogram import Bot
from django.core.management import call_command


class Command(BaseCommand):
    help = "Run Django server and set Telegram webhook (local with ngrok)"

    def handle(self, *args, **options):
        public_url = os.getenv("WEBHOOK_URL", "http://127.0.0.1:8000/webhook/")

        bot = Bot(token=settings.BOT_TOKEN)
        asyncio.run(bot.set_webhook(public_url))
        self.stdout.write(self.style.SUCCESS(f"Webhook set to {public_url}"))

        call_command("runserver", "0.0.0.0:8000")
