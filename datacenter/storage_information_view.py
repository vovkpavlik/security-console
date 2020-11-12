from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime, timedelta

def get_duration(person):
    return localtime() - localtime(person.entered_at)


def is_strange(visit, minutes):
    return get_duration(visit) > timedelta(minutes=minutes)


def storage_information_view(request):
    non_closed_visits = []
    not_leaved = Visit.objects.filter(leaved_at=None)
    for visit in not_leaved:
        visits_info = {"who_entered": visit.passcard,
                       "entered_at": visit.entered_at,
                       "duration": get_duration(visit),
                       "is_strange": is_strange(visit, minutes=60)
                       }
        non_closed_visits.append(visits_info)
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)





