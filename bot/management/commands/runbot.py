from django.core.management.base import BaseCommand
from bot.main import dp, bot
import asyncio


class Command(BaseCommand):
    help = 'Run the Telegram bot'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting bot with polling...'))

        async def main():
            await dp.start_polling(bot)

        asyncio.run(main())