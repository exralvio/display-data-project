# Generated by Django 4.2.9 on 2024-01-31 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('modification_time', models.DateTimeField(auto_now=True)),
                ('delivered_quantity', models.IntegerField(null=True)),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.orderitem')),
            ],
            options={
                'db_table': 'delivery',
            },
        ),
    ]
