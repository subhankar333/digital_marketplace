# Generated by Django 4.2.4 on 2023-08-09 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_order_detail_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total_sales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='total_sales_amount',
            field=models.IntegerField(default=0),
        ),
    ]
