import os
import sys
import django
from django.utils.timezone import localtime
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()


from datacenter.models import Passcard, Visit


def get_duration(visit):
    """
    Returns the time spent by an employee in the storage in seconds (int)

    Parameters
    ----------
    visit : <class 'datacenter.models.Visit'>
    """
    entered_at_localtime = localtime(visit.entered_at)
    current_localtime = localtime()
    datetime_delta = current_localtime - entered_at_localtime

    return int(datetime_delta.total_seconds())


def seconds_to_str(seconds):
    mm, ss = divmod(seconds, 60)
    hh, mm = divmod(mm, 60)
    return '{0:02d}:{1:02d}:{2:02d}'.format(hh, mm, ss)


if __name__ == "__main__":
    visits_not_leaved = Visit.objects.filter(leaved_at__isnull=True)
    for visit_not_leaved in visits_not_leaved:
        print(visit_not_leaved)
        print("Зашёл в хранилище, время по Москве:", localtime(visit_not_leaved.entered_at), sep='\n')
        time.sleep(10)
        time_delta_seconds = get_duration(visit_not_leaved)
        print("\nНаходится в хранилище:", seconds_to_str(time_delta_seconds), sep='\n')
