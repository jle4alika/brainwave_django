# Generated by Django 5.2.1 on 2025-05-14 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='surname',
        ),
    ]
