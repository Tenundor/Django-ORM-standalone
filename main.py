import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Passcard, Visit


if __name__ == "__main__":
    # Программируем здесь
    passcards = Passcard.objects.all()
    active_passcards = Passcard.objects.filter(is_active=True)
    print("Всего пропусков", len(passcards))
    print("Активных пропусков", len(active_passcards))