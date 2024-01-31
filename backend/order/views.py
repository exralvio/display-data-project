from django.http import JsonResponse

from order.models import Order
from order.utils import delivered_amount, order_amount


def get_orders(request):
    orders = Order.objects.all()

    response = []
    for order in orders:
        response.append({
            'id': order.id,
            'order_name': order.order_name,
            'customer_name': order.customer.name,
            'company_name': order.customer.customer_company.company_name,
            'created_at': order.created_at,
            'delivered_amount': delivered_amount(order.id),
            'total_amount': order_amount(order.id)
        })
    return JsonResponse({'orders': response})
