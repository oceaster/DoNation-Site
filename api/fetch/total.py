from api.models import Pledge
from django.db.models import Sum


def co2():
    return Pledge.objects.aggregate(Sum('save_co2'))
