# Generated by Django 2.1.11 on 2019-11-01 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("common", "0037_auto_20191011_2021")]

    operations = [
        migrations.AddField(
            model_name="repository",
            name="use_analyze_char",
            field=models.BooleanField(default=False, verbose_name="Use analyze char"),
        ),
        migrations.AddField(
            model_name="repositoryupdate",
            name="use_analyze_char",
            field=models.BooleanField(default=False),
        ),
    ]
