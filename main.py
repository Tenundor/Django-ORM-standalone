import os
import sys
import django
import asyncio
from datacenter.models import Passcard, Visit


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()


async def print_visits_not_leaved():
    visits_not_leaved = None
    while True:
        visits_not_leaved_updated = Visit.objects.filter(leaved_at__isnull=True)
        if str(visits_not_leaved_updated) != str(visits_not_leaved):
            print(visits_not_leaved_updated)
            visits_not_leaved = visits_not_leaved_updated
        await asyncio.sleep(1000)


if __name__ == "__main__":
    asyncio.run(print_visits_not_leaved())
