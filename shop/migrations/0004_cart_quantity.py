# Generated by Django 2.1.4 on 2019-05-29 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_cartitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]