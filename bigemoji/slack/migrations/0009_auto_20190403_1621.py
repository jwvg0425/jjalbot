# Generated by Django 2.1.7 on 2019-04-03 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("slack", "0008_move_slack_account")]

    operations = [
        migrations.AlterUniqueTogether(
            name="slackaccountdeprecated", unique_together=set()
        ),
        migrations.RemoveField(model_name="slackaccountdeprecated", name="account"),
        migrations.RemoveField(model_name="slackaccountdeprecated", name="team"),
        migrations.AlterUniqueTogether(
            name="slacktokendeprecated", unique_together=set()
        ),
        migrations.RemoveField(model_name="slacktokendeprecated", name="account"),
        migrations.RemoveField(model_name="slacktokendeprecated", name="app"),
        migrations.DeleteModel(name="SlackAccountDeprecated"),
        migrations.DeleteModel(name="SlackTeam"),
        migrations.DeleteModel(name="SlackTokenDeprecated"),
    ]
