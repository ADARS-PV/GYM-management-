# Generated by Django 5.1.1 on 2024-10-23 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0006_dailyclass_is_recurring'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyclass',
            name='is_recurring',
        ),
    ]