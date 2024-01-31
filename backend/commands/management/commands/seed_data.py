import csv

from django.core.management import BaseCommand

from customer.models import CustomerCompany, Customer
from delivery.models import Delivery
from order.models import Order, OrderItem


class Command(BaseCommand):
    help = "Execute the seeder"

    def handle(self, *args, **options):
        seeder = [
            {
                "path": './seeder/Test task - Postgres - customer_companies.csv',
                "func": self.import_customer_company
            },
            {
                "path": './seeder/Test task - Postgres - customers.csv',
                "func": self.import_customer
            },
            {
                "path": './seeder/Test task - Postgres - deliveries.csv',
                "func": self.import_delivery
            },
            {
                "path": './seeder/Test task - Postgres - orders.csv',
                "func": self.import_order
            },
            {
                "path": './seeder/Test task - Postgres - order_items.csv',
                "func": self.import_order_item
            }
        ]

        for seed in seeder:
            results = self.read_csv_file(seed['path'])
            seed['func'](results)

        self.stdout.write(self.style.SUCCESS('Successfully executed.'))

    @staticmethod
    def read_csv_file(file_path):
        results = []
        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for row in csv_reader:
                results.append(row)
        return results

    def import_customer_company(self, datas):
        for data in datas:
            key, company_name = data
            CustomerCompany.objects.create(id=key, company_name=company_name)
        self.stdout.write(self.style.SUCCESS(f'Customer Company created'))

    def import_customer(self, datas):
        for data in datas:
            user_id, login, password, name, customer_company_id, credit_cards = data
            Customer.objects.create(user_id=user_id, login=login, password=password, name=name,
                                    customer_company_id=customer_company_id, credit_cards=credit_cards)
        self.stdout.write(self.style.SUCCESS(f'Customer created'))

    def import_order(self, datas):
        for data in datas:
            key, created_at, order_name, customer_id = data
            Order.objects.create(id=key, order_name=order_name, customer_id=customer_id, created_at=created_at)
        self.stdout.write(self.style.SUCCESS(f'Order created'))

    def import_order_item(self, datas):
        for data in datas:
            key, order_id, price_per_unit, quantity, product = data
            if price_per_unit == '':
                price_per_unit = None
            OrderItem.objects.create(id=key, order_id=order_id, price_per_unit=price_per_unit, quantity=quantity,
                                     product=product)
        self.stdout.write(self.style.SUCCESS(f'Order Item created'))

    def import_delivery(self, datas):
        for data in datas:
            key, order_item_id, delivered_quantity = data
            Delivery.objects.create(id=key, order_item_id=order_item_id, delivered_quantity=delivered_quantity)
        self.stdout.write(self.style.SUCCESS(f'Delivery created'))
