import asyncio, os
from django.core.management.base import BaseCommand
from bot.main import bot


class Command(BaseCommand):
    help = "Set Telegram webhook"

    def handle(self, *args, **options):
        public_url = os.getenv("WEBHOOK_URL")
        asyncio.run(bot.set_webhook(public_url))
        self.stdout.write(self.style.SUCCESS(f"Webhook set to {public_url}"))
