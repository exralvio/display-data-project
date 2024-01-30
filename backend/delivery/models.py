from django.db import models

from common.models import DisplayData


class Delivery(DisplayData):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    order_item_id = models.IntegerField(null=True)
    delivered_quantity = models.IntegerField(null=True)

    class Meta:
        db_table = 'delivery'
