import os
import sys
import django
from django.utils.timezone import localtime
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()


from datacenter.models import Passcard, Visit


def calculate_storage_time(visit):
    """
    Returns the time spent by an employee in the storage in the format:

    Находится в хранилище:
    hh:mm:ss

    Parameters
    ----------
    visit : <class 'datacenter.models.Visit'>
    """


def seconds_to_str(seconds):
    mm, ss = divmod(seconds, 60)
    hh, mm = divmod(mm, 60)
    return '{0:2d}:{1:2d}:{2:2d}'.format(hh, mm, ss)


if __name__ == "__main__":
    visits_not_leaved = Visit.objects.filter(leaved_at__isnull=True)
    for visit in visits_not_leaved:
        print(visit.passcard)
        entered_at_localtime = localtime(visit.entered_at)
        print("Зашёл в хранилище, время по Москве:", entered_at_localtime, sep='\n')
        current_localtime = localtime()
        datetime_delta = current_localtime - entered_at_localtime
        total_delta_seconds = int(datetime_delta.total_seconds())
        time.sleep(5000)
        print("\nНаходится в хранилище:", seconds_to_str(total_delta_seconds), sep='\n')
