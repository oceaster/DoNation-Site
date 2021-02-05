from django.http import JsonResponse
from .post.pledge import new_pledge
from .fetch.pledge import fetch_pledges
from .fetch.total import co2

# ========== FETCH API VIEWS ========== #


def fetch_user_pledges(req, uid, *args, **kwargs):
    return JsonResponse(fetch_pledges(uid))


def fetch_total_co2(req, *args, **kwargs):
    return JsonResponse(co2())


# ========== POST API VIEWS ========== #


def post_user_pledge(req, uid, pledge, co2, *args, **kwargs):
    return JsonResponse(
        new_pledge(uid, pledge, co2)
    )
