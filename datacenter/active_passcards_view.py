from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def active_passcards_view(request):
    all_cards = Passcard.objects.all()
    active_passcards = Passcard.objects.filter(is_active=True)

    all_passcards = Passcard.objects.all()
    context = {
        "active_passcards": active_passcards,  # люди с активными пропусками
    }
    return render(request, 'active_passcards.html', context)
