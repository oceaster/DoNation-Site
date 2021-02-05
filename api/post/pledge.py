from api.models import Pledge


def new_pledge(uid, pledge, co2):
    try:
        Pledge.objects.create(
            uid=uid,
            pledge=pledge,
            save_co2=co2
        )
        return {'message': 'success!'}
    except Exception as e:
        return {'message': str(e)}
