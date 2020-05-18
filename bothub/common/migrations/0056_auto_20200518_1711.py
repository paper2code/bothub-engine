# Generated by Django 2.1.11 on 2020-05-18 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("common", "0055_auto_20200518_0951")]

    operations = [
        migrations.AlterField(
            model_name="repository",
            name="algorithm",
            field=models.CharField(
                choices=[
                    (
                        "neural_network_internal",
                        "Neural Network with internal vocabulary",
                    ),
                    (
                        "neural_network_external",
                        "Neural Network with external vocabulary (BETA)",
                    ),
                    (
                        "transformer_network_diet",
                        "Transformer Neural Network with internal vocabulary",
                    ),
                    (
                        "transformer_network_diet_word_embedding",
                        "Transformer Neural Network with word embedding external vocabulary",
                    ),
                ],
                default="neural_network_internal",
                max_length=50,
                verbose_name="algorithm",
            ),
        )
    ]
