# Generated by Django 4.2.4 on 2023-08-05 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_order_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_detail',
            name='customer_email',
        ),
    ]
