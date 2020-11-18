import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Passcard, Visit


if __name__ == "__main__":
    # Программируем здесь
    passcards = Passcard.objects.all()
    some_passcard = passcards[1]
    print("Owner name:", some_passcard.owner_name)
    print("Passcode:", some_passcard.passcode)
    print("Created at:", some_passcard.created_at)
    print("Is active:", some_passcard.is_active)