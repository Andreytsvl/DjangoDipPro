from django import template
from basket_app.models import Basket
#from basket.utils import get_user_carts

register = template.Library()


@register.simple_tag()
def user_baskets(request):
    if request.user.is_authenticated:
        return Basket.objects.filter(user=request.user)
    #return get_user_baskets(request)