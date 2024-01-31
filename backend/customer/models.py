from django.db import models

from common.models import DisplayData


class CustomerCompany(DisplayData):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    company_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'customer_company'


class Customer(DisplayData):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    user_id = models.CharField(max_length=255, unique=True)
    login = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    customer_company = models.ForeignKey(CustomerCompany, on_delete=models.CASCADE)
    credit_cards = models.TextField()

    class Meta:
        db_table = 'customer'
