# Generated by Django 3.1.3 on 2020-11-19 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20201120_0021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='room',
            new_name='rooms',
        ),
    ]
