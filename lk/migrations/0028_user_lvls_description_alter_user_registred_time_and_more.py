# Generated by Django 5.2.1 on 2025-05-17 19:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0027_alter_user_registred_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_lvls',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='registred_time',
            field=models.DateField(default=datetime.datetime(2025, 5, 18, 2, 15, 12, 284832)),
        ),
        migrations.AlterField(
            model_name='user_achivements',
            name='passed_time',
            field=models.DateField(default=datetime.datetime(2025, 5, 18, 2, 15, 12, 287344)),
        ),
    ]
