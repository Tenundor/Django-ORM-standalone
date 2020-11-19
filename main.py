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


def get_duration_adv(visit):
    if visit.leaved_at is None:
        entered_at_localtime = localtime(visit.entered_at)
        current_localtime = localtime()
        datetime_delta = current_localtime - entered_at_localtime

        return int(datetime_delta.total_seconds())
    else:
        visit_duration_time = visit.leaved_at - visit.entered_at

        return int(visit_duration_time.total_seconds())


def seconds_to_str(seconds):
    mm, ss = divmod(seconds, 60)
    hh, mm = divmod(mm, 60)
    return '{0:02d}:{1:02d}:{2:02d}'.format(hh, mm, ss)


def is_visit_long(visit, minutes=10):
    visit_duration_minutes = get_duration_adv(visit) // 60
    if visit_duration_minutes > minutes:
        return True
    else:
        return False



if __name__ == "__main__":
    visits_not_leaved = Visit.objects.filter(leaved_at__isnull=True)
    for visit_not_leaved in visits_not_leaved:
        print(get_duration_adv(visit_not_leaved))
        print(type(visit_not_leaved.leaved_at))
        print(visit_not_leaved)
        print("Зашёл в хранилище, время по Москве:", localtime(visit_not_leaved.entered_at), sep='\n')
        #time.sleep(10)
        time_delta_seconds = get_duration(visit_not_leaved)
        print("\nНаходится в хранилище:", seconds_to_str(time_delta_seconds), sep='\n')
    some_passcard = Passcard.objects.all()[1]
    visits_of_some_person = Visit.objects.filter(passcard=some_passcard)
    print(type(visits_of_some_person[0].leaved_at))
    print(get_duration_adv(visits_of_some_person[0]))
    all_visits = Visit.objects.all()
    visits_more_60_minutes = []
    for visit in all_visits:
        if is_visit_long(visit, minutes=60):
            visits_more_60_minutes.append(visit)
    print("Визиты дольше 60 мин", visits_more_60_minutes)
