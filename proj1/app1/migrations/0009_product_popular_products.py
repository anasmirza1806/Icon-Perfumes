# Generated by Django 4.2.6 on 2024-02-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_product_new_arrival'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='popular_products',
            field=models.CharField(default='', max_length=20),
        ),
    ]
