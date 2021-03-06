import base64

from django.conf import settings
from django.core.management.base import BaseCommand

from bothub.common.models import RepositoryNLPTrain
from bothub.utils import send_bot_data_file_aws


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if settings.AWS_SEND:
            repo = RepositoryNLPTrain.objects.all().exclude(bot_data__exact="")
            for update in repo:
                try:
                    repository_update = RepositoryNLPTrain.objects.get(pk=update.pk)
                    bot_data = send_bot_data_file_aws(
                        update.pk, base64.b64decode(update.bot_data)
                    )
                    repository_update.bot_data = bot_data
                    repository_update.save(update_fields=["bot_data"])
                    print(
                        "Updating bot_data repository_update {}".format(str(update.pk))
                    )
                except Exception as e:
                    print("Error " + str(update.pk))
                    print(str(e))
        else:
            print("You need to configure the environment variables for AWS.")
