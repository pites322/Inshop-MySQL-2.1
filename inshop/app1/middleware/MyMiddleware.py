from django.conf import settings
from django.contrib import auth
from django.contrib.auth import load_backend
from django.contrib.auth.backends import RemoteUserBackend
from django.core.exceptions import ImproperlyConfigured
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from app1.models import ShoppingList


def get_user(request):
    if not hasattr(request, '_cached_user'):
        request._cached_user = auth.get_user(request)
    return request._cached_user


class GetBasketState(MiddlewareMixin):
    def process_request(self, request):
        assert hasattr(request, 'session')
        user = SimpleLazyObject(lambda: get_user(request))
        purchases = ShoppingList.objects.all()
        purchase_amount = 0
        for purchase in purchases:
            if purchase.buyer_id == user.id and purchase.payed_or_not == "No":
                purchase_amount = purchase_amount + purchase.price
            else:
                pass
        user.basket_state = purchase_amount
