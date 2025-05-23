# Generated by Django 5.2.1 on 2025-05-14 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0004_user_lvls_achivement_description_achivement_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_courses',
            old_name='lvl',
            new_name='difficulty',
        ),
        migrations.AddField(
            model_name='user_courses',
            name='lvls',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='registred_time',
            field=models.DateField(default=datetime.datetime(2025, 5, 14, 16, 15, 49, 266623)),
        ),
    ]
