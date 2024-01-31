from django.db import models

from common.models import DisplayData
from customer.models import Customer


class Order(DisplayData):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    order_name = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        db_table = 'order'


class OrderItem(DisplayData):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    quantity = models.IntegerField()
    product = models.CharField(max_length=255)

    class Meta:
        db_table = 'order_item'
