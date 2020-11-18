import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Passcard, Visit


if __name__ == "__main__":
    # Программируем здесь
    visits_not_leaved = Visit.objects.filter(leaved_at__isnull=True)
    print(visits_not_leaved)