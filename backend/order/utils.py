from delivery.models import Delivery
from order.models import OrderItem


def delivered_amount(order_id):
    order_item_ids = OrderItem.objects.filter(order_id=order_id).values_list('id', flat=True)
    delivered = Delivery.objects.filter(order_item__in=order_item_ids)

    total_amount = 0
    for deliver in delivered:
        amount = 0
        price = deliver.order_item.price_per_unit
        if price:
            amount = price * deliver.delivered_quantity
        total_amount += amount

    return float(total_amount)


def order_amount(order_id):
    order_items = OrderItem.objects.filter(order_id=order_id)

    total_amount = 0
    for order_item in order_items:
        price = order_item.price_per_unit
        if price:
            total_amount += price * order_item.quantity

    return float(total_amount)
