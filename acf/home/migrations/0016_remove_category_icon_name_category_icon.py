# Generated by Django 4.2.16 on 2024-09-29 10:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0026_delete_uploadedimage"),
        ("home", "0015_projecttype_icon"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="icon_name",
        ),
        migrations.AddField(
            model_name="category",
            name="icon",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Ikona",
            ),
        ),
    ]
