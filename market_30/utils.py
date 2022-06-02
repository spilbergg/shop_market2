from new_app.models import Person
from market_30.models import Shop


def get_shop(shop_id):
    if shop_id:
        return Shop.objects.filter(pk=shop_id).first()


def validate_name(name):
    return len(name) == 0

def validate_name_uniq(a):
    log = Person.objects.filter(login=a['login'])
    if log:
        return True
    else:
        pass