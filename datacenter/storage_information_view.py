from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []
    not_leaved = Visit.objects.filter(leaved_at=None)
    for visit in not_leaved:
        visits_info = {"who_entered": visit.passcard,
                       "entered_at": visit.entered_at,
                       "duration": visit.get_duration(),
                       "is_strange": visit.is_visit_long(60)
                       }
        non_closed_visits.append(visits_info)
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)





