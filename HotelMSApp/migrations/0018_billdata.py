# Generated by Django 3.1.8 on 2024-04-04 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelMSApp', '0017_delete_billdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.IntegerField()),
                ('table', models.IntegerField()),
                ('room', models.IntegerField()),
                ('customer', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('address', models.CharField(max_length=100)),
                ('cheakindate', models.DateField()),
                ('cheakintime', models.TimeField()),
                ('cheakoutdate', models.DateField()),
                ('cheakouttime', models.TimeField()),
                ('decription', models.CharField(max_length=50)),
                ('quntity', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('totalamount', models.IntegerField()),
                ('gstamount', models.IntegerField()),
                ('netamount', models.IntegerField()),
                ('timestap', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]