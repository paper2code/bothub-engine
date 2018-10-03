from django.contrib import admin

from .models import RepositoryCategory
from .models import Repository
from .models import RepositoryUpdate
from .models import RepositoryExample
from .models import RepositoryExampleEntity
from .models import RepositoryTranslatedExample
from .models import RepositoryTranslatedExampleEntity
from .models import RepositoryAuthorization


@admin.register(RepositoryCategory)
class RepositoryCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):
    pass


@admin.register(RepositoryUpdate)
class RepositoryUpdateAdmin(admin.ModelAdmin):
    list_display_links = [
        'id',
        '__str__',
    ]
    list_display = [
        'id',
        '__str__',
        'repository',
        'language',
        'training_started_at',
        'trained_at',
        'failed_at',
    ]
    readonly_fields = [
        'training_log',
    ]


@admin.register(RepositoryExample)
class RepositoryExampleAdmin(admin.ModelAdmin):
    pass


@admin.register(RepositoryExampleEntity)
class RepositoryExampleEntityAdmin(admin.ModelAdmin):
    pass


@admin.register(RepositoryTranslatedExample)
class RepositoryTranslatedExampleAdmin(admin.ModelAdmin):
    pass


@admin.register(RepositoryTranslatedExampleEntity)
class RepositoryTranslatedExampleEntity(admin.ModelAdmin):
    pass


@admin.register(RepositoryAuthorization)
class RepositoryAuthorizationAdmin(admin.ModelAdmin):
    pass
