# Generated by Django 5.2.1 on 2025-05-15 16:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0009_alter_user_image_alter_user_registred_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='achivement',
            name='image',
            field=models.ImageField(default='avatar.png', upload_to='achievements/'),
        ),
        migrations.AddField(
            model_name='user_achivements',
            name='image',
            field=models.ImageField(default='avatar.png', upload_to='achievements/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='avatar.png', upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='registred_time',
            field=models.DateField(default=datetime.datetime(2025, 5, 15, 23, 13, 35, 608638)),
        ),
    ]
