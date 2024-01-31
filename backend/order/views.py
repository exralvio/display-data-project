from django.http import JsonResponse

from order.models import Order


def get_orders(request):
    orders = Order.objects.all()
    order_list = list(orders.values())
    return JsonResponse({'orders': order_list})
