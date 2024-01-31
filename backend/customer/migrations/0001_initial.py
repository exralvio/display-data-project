# Generated by Django 4.2.9 on 2024-01-31 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('modification_time', models.DateTimeField(auto_now=True)),
                ('company_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'customer_company',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('modification_time', models.DateTimeField(auto_now=True)),
                ('user_id', models.CharField(max_length=255, unique=True)),
                ('login', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('company_id', models.IntegerField()),
                ('credit_cards', models.TextField()),
                ('customer_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customercompany')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
