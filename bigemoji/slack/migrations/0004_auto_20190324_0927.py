# Generated by Django 2.1.7 on 2019-03-24 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slack', '0003_auto_20190324_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='slackaccount',
            name='date_created',
            field=models.DateTimeField(auto_now=True, verbose_name='date created'),
        ),
        migrations.AddField(
            model_name='slackteam',
            name='date_created',
            field=models.DateTimeField(auto_now=True, verbose_name='date created'),
        ),
    ]