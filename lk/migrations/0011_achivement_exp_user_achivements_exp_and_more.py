# Generated by Django 5.2.1 on 2025-05-15 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0010_achivement_image_user_achivements_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='achivement',
            name='exp',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_achivements',
            name='exp',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='registred_time',
            field=models.DateField(default=datetime.datetime(2025, 5, 15, 23, 22, 2, 614488)),
        ),
    ]
