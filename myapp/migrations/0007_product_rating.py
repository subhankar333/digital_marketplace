# Generated by Django 4.2.4 on 2023-08-09 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_product_total_sales_product_total_sales_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=4.3),
            preserve_default=False,
        ),
    ]