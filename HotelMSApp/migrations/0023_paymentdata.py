# Generated by Django 3.1.8 on 2024-04-07 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelMSApp', '0022_delete_paymentdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zipcode', models.IntegerField()),
                ('paymenttype', models.CharField(max_length=30)),
                ('nameascard', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('timestap', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
