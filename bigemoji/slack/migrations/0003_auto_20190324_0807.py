# Generated by Django 2.1.7 on 2019-03-24 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("slack", "0002_auto_20190323_1741")]

    operations = [
        migrations.AlterField(
            model_name="slackteam",
            name="delete_eta",
            field=models.IntegerField(default=604800),
        )
    ]
