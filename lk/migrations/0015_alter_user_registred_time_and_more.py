# Generated by Django 5.2.1 on 2025-05-16 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0014_alter_user_registred_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='registred_time',
            field=models.DateField(default=datetime.datetime(2025, 5, 16, 20, 56, 23, 77214)),
        ),
        migrations.AlterField(
            model_name='user_achivements',
            name='passed_time',
            field=models.DateField(default=datetime.datetime(2025, 5, 16, 20, 56, 23, 77214)),
        ),
    ]
