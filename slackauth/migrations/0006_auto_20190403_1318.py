# Generated by Django 2.1.7 on 2019-04-03 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("slackauth", "0005_slacktoken_extra_data")]

    operations = [
        migrations.AlterField(
            model_name="slacktoken",
            name="account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="slackauth.SlackAccount"
            ),
        )
    ]
