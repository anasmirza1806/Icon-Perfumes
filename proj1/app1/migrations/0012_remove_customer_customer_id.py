# Generated by Django 4.2.6 on 2024-03-04 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_remove_customer_address_line1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='customer_id',
        ),
    ]
