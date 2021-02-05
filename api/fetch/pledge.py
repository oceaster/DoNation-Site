from api.models import Pledge


def create_pledge_dict(db_object):
    if db_object is None:
        return {
            'error': 'invalid request'
        }

    return {
        'id': db_object.id,
        'uid': db_object.uid,
        'pledge': db_object.pledge,
        'co2': db_object.save_co2,
        'timestamp': db_object.timestamp,
    }


def fetch_pledges(uid):
    try:
        entries = Pledge.objects.filter(uid=uid)
        pledges = [create_pledge_dict(obj) for obj in entries]
        return {'data': pledges}
    except Exception as e:
        return {'error': str(e)}
