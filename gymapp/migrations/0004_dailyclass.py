# Generated by Django 5.1.1 on 2024-10-23 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0003_alter_trainer_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('workout_type', models.CharField(max_length=100)),
                ('video_url', models.URLField()),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymapp.trainer')),
            ],
        ),
    ]
