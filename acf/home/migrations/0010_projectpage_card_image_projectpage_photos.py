# Generated by Django 4.2.16 on 2024-09-25 11:26

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0026_delete_uploadedimage"),
        ("home", "0009_homepage_financer_disclaimer"),
    ]

    operations = [
        migrations.AddField(
            model_name="projectpage",
            name="card_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
        migrations.AddField(
            model_name="projectpage",
            name="photos",
            field=wagtail.fields.StreamField(
                [("image", 0)],
                blank=True,
                block_lookup={
                    0: (
                        "wagtail.images.blocks.ImageChooserBlock",
                        (),
                        {"label": "Slika"},
                    )
                },
                null=True,
                verbose_name="Slike",
            ),
        ),
    ]
