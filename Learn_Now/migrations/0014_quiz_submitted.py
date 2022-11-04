# Generated by Django 3.1.4 on 2022-01-11 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Learn_Now', '0013_auto_20220108_0248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz_submitted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assign_num', models.IntegerField(default=0)),
                ('ans_1', models.BooleanField()),
                ('ans_2', models.BooleanField()),
                ('ans_3', models.BooleanField()),
                ('ans_4', models.BooleanField()),
                ('ans_5', models.BooleanField()),
                ('course', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='quiz_course', to='Learn_Now.course')),
                ('student', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
