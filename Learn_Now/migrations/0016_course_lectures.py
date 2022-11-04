# Generated by Django 3.1.4 on 2022-01-19 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Learn_Now', '0015_auto_20220118_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Lectures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture', models.IntegerField(blank=True)),
                ('intro_vid', models.URLField(blank=True, max_length=220)),
                ('course', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Lecture_course', to='Learn_Now.course')),
            ],
        ),
    ]
