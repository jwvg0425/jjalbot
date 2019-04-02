# Generated by Django 2.1.7 on 2019-04-02 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slackauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slacktoken',
            name='token_type',
            field=models.IntegerField(choices=[(0, 'User token'), (1, 'Bot token'), (2, 'Workspace token'), (3, 'Legacy token'), (4, 'Verification token')], default=0),
            preserve_default=False,
        ),
    ]