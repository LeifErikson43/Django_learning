# Generated by Django 3.1.4 on 2022-01-19 03:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Learn_Now', '0021_auto_20220119_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignments',
            name='student',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='assignment_student', to=settings.AUTH_USER_MODEL),
        ),
    ]