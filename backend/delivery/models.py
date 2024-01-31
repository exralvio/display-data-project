from django.db import models

from common.models import DisplayData
from order.models import OrderItem


class Delivery(DisplayData):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    delivered_quantity = models.IntegerField(null=True)

    class Meta:
        db_table = 'delivery'
