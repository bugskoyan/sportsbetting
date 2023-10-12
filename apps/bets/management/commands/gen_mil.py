
from typing import Any
import random
from django.core.management.base import BaseCommand
from bets.models import Bookmaker


BOOK_RAND = [
    "Bet365", "William Hill", "Ladbrokes", "Paddy Power", "888sport",
    "Betfair", "Unibet", "Bwin", "Betway", "Coral",
    "10Bet", "SportPesa", "BetOnline", "Intertops", "BetVictor",
    "Boylesports", "Betfred", "888casino", "Bet-at-Home", "BetUS",
    "Betsson", "BetSafe", "BetAmerica", "Betdaq", "BetRivers",
    "BetRegal", "BetStars", "Betvictor Casino", "Borgata", "Caesars Sportsbook",
    "FanDuel", "Fox Bet", "Golden Nugget", "Hard Rock", "PointsBet",
    "Resorts Casino", "SugarHouse", "TwinSpires", "Virgin Bet", "Xpressbet",
    "BetHard", "Betway Casino", "DraftKings", "Parx Casino", "theScore Bet",
    "Tipico", "TVG", "WynnBET", "YouWager"
]




class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        num_objects_to_create = 100  # Количество объектов для создания

        # Создаем список объектов для bulk_create
        objects_to_create = []
        for _ in range(num_objects_to_create):
            objects_to_create.append(Bookmaker(name = random.choice(BOOK_RAND), contact_info = f"{random.randint(1, 999)} {random.choice(['Main St', 'Park Ave', 'Elm St'])}, City, +7-777-555-{random.randint(1000, 9999)}"))

        try:
            # Выполняем bulk_create для создания объектов
            Bookmaker.objects.bulk_create(objects_to_create, batch_size=1000)  # batch_size можете настроить по вашему усмотрению
            self.stdout.write(self.style.SUCCESS(f'Успешно создано {num_objects_to_create} объектов'))
        except Exception as exc:
            self.stderr.write(self.style.ERROR(f'Ошибка при создании объектов: {str(exc)}'))