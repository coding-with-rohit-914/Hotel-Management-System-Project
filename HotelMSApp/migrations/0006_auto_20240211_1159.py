# Generated by Django 3.0.5 on 2024-02-11 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelMSApp', '0005_auto_20240211_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookroomdata',
            name='idprroffile',
            field=models.FileField(max_length=254, upload_to=''),
        ),
    ]
