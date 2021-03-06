# Generated by Django 2.2.12 on 2020-08-31 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0006_auto_20200729_1220"),
        ("common", "0083_repositoryintent_created_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="RepositoryReports",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("count_reports", models.IntegerField(default=0)),
                ("report_date", models.DateField(verbose_name="report date")),
                (
                    "repository_version_language",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="repository_reports",
                        to="common.RepositoryVersionLanguage",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="authentication.RepositoryOwner",
                    ),
                ),
            ],
            options={
                "verbose_name": "repository report",
                "verbose_name_plural": "repository reports",
            },
        )
    ]
