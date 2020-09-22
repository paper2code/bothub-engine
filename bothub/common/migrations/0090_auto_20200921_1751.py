# Generated by Django 2.2.16 on 2020-09-21 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0089_remove_repository_allow_search_examples'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repositoryintent',
            name='repository_version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='version_intents', to='common.RepositoryVersion'),
        ),
    ]