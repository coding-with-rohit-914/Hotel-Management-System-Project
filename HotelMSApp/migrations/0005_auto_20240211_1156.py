# Generated by Django 3.0.5 on 2024-02-11 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelMSApp', '0004_roomfeedbackdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookroomdata',
            name='idprroffile',
            field=models.ImageField(max_length=254, upload_to=''),
        ),
    ]