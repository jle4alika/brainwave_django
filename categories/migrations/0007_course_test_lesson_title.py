# Generated by Django 5.2.1 on 2025-05-17 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0006_alter_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_test',
            name='lesson_title',
            field=models.CharField(default='', max_length=255),
        ),
    ]
