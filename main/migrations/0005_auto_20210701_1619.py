# Generated by Django 3.1 on 2021-07-01 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210701_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='addtocart',
        ),
        migrations.AddField(
            model_name='orderitems',
            name='addtocart',
            field=models.BooleanField(default=False),
        ),
    ]
