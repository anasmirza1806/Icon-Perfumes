# Generated by Django 4.2.6 on 2024-03-29 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_remove_order_customer_id_remove_order_order_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
