# Generated by Django 3.0.5 on 2024-02-13 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelMSApp', '0011_paymentdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookroomdata',
            name='idprroffile',
            field=models.ImageField(upload_to=''),
        ),
    ]
