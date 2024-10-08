# Generated by Django 4.2.16 on 2024-09-25 12:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0026_delete_uploadedimage"),
        ("home", "0010_projectpage_card_image_projectpage_photos"),
    ]

    operations = [
        migrations.CreateModel(
            name="GenericSocialMediaSettings",
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
                (
                    "financer_disclaimer",
                    models.TextField(blank=True, verbose_name="Disclaimer financerja"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="financer_disclaimer",
        ),
        migrations.AlterField(
            model_name="projectpage",
            name="card_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Slika na kartici",
            ),
        ),
    ]
