# Generated by Django 2.1.7 on 2019-03-29 14:08

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
        ('bigemoji', '0009_bigemojistorage'),
        ('slack', '0004_auto_20190324_0927'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SlackAccount',
            new_name='SlackAccountDeprecated',
        ),
        migrations.RenameModel(
            old_name='SlackToken',
            new_name='SlackTokenDeprecated',
        ),
    ]
