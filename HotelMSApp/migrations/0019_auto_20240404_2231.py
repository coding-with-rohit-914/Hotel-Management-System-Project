# Generated by Django 3.1.8 on 2024-04-04 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelMSApp', '0018_billdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billdata',
            name='quntity',
            field=models.BigIntegerField(),
        ),
    ]