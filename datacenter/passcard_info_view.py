from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    this_person = Passcard.objects.get(passcode=passcode)
    data_person = Visit.objects.filter(passcard=this_person)
    this_passcard_visits = []
    for visit in data_person:
        visits = {
                "entered_at": visit.entered_at,
                "duration": visit.get_duration(),
                "is_strange": visit.is_visit_long(60)
        }
        this_passcard_visits.append(visits)
    context = {
        "passcard": this_person,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)