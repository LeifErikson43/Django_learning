# Generated by Django 3.1.4 on 2022-01-08 01:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Learn_Now', '0011_course_course_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='current_students',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
