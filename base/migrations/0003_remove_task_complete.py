# Generated by Django 3.0.9 on 2022-01-18 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20210322_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='complete',
        ),
    ]
