# Generated by Django 2.1.11 on 2019-12-12 20:13

from django.db import migrations

from bothub.common import languages


def noop(apps, schema_editor):  # pragma: no cover
    pass


def current_version(
    repository, repositoryversionlanguage, language=None, is_default=True
):
    language = language or repository.language

    repository_version, created = repository.versions.get_or_create(
        is_default=is_default
    )

    repository_version_language, created = repositoryversionlanguage.objects.get_or_create(
        repository_version=repository_version, language=language
    )
    return repository_version_language


def migrate_data(apps, schema_editor):  # pragma: no cover
    Repository = apps.get_model("common", "Repository")
    RepositoryVersionLanguage = apps.get_model("common", "RepositoryVersionLanguage")
    RepositoryUpdate = apps.get_model("common", "RepositoryUpdate")
    RepositoryExample = apps.get_model("common", "RepositoryExample")
    RepositoryEvaluate = apps.get_model("common", "RepositoryEvaluate")
    RepositoryEvaluateResult = apps.get_model("common", "RepositoryEvaluateResult")
    RepositoryTranslatedExample = apps.get_model(
        "common", "RepositoryTranslatedExample"
    )

    for repo in Repository.objects.all():
        for lang in languages.VERBOSE_LANGUAGES.keys():
            update = RepositoryUpdate.objects.filter(
                repository=repo, trained_at__isnull=False, language=lang
            ).last()

            if update is None:
                update = RepositoryUpdate.objects.filter(
                    repository=repo, language=lang
                ).last()
                if update is None:
                    continue

            version_language = current_version(
                repository=Repository.objects.get(pk=update.repository.pk),
                repositoryversionlanguage=RepositoryVersionLanguage,
                language=update.language,
            )

            version_language.bot_data = update.bot_data
            version_language.training_started_at = update.training_started_at
            version_language.training_end_at = update.trained_at
            version_language.failed_at = update.failed_at
            version_language.use_analyze_char = update.use_analyze_char
            version_language.use_name_entities = update.use_name_entities
            version_language.use_competing_intents = update.use_competing_intents
            version_language.algorithm = update.algorithm
            version_language.training_log = update.training_log
            version_language.last_update = update.trained_at
            version_language.save(
                update_fields=[
                    "bot_data",
                    "training_started_at",
                    "training_end_at",
                    "failed_at",
                    "use_analyze_char",
                    "use_name_entities",
                    "use_competing_intents",
                    "algorithm",
                    "training_log",
                    "last_update",
                ]
            )

            RepositoryExample.objects.filter(
                repository_update__repository=repo, repository_update__language=lang
            ).update(
                repository_update=update, repository_version_language=version_language
            )
            RepositoryEvaluate.objects.filter(
                repository_update__repository=repo, repository_update__language=lang
            ).update(
                repository_update=update, repository_version_language=version_language
            )
            RepositoryEvaluateResult.objects.filter(
                repository_update__repository=repo, repository_update__language=lang
            ).update(
                repository_update=update, repository_version_language=version_language
            )
            RepositoryTranslatedExample.objects.filter(
                repository_update__repository=repo, repository_update__language=lang
            ).update(
                repository_update=update, repository_version_language=version_language
            )


class Migration(migrations.Migration):
    dependencies = [("common", "0042_auto_20191212_2013")]

    operations = [migrations.RunPython(migrate_data, noop)]
