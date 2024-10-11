# Generated by Django 4.2.16 on 2024-09-23 16:20

import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_alter_homepage_introduction"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.TextField(blank=True, verbose_name="Ime kategorije")),
            ],
        ),
        migrations.CreateModel(
            name="ProjectType",
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
                ("name", models.TextField(blank=True, verbose_name="Tip projekta")),
            ],
        ),
        migrations.AlterField(
            model_name="projectpage",
            name="contact",
            field=models.TextField(blank=True, verbose_name="Kontakt vodje projekta"),
        ),
        migrations.AlterField(
            model_name="projectpage",
            name="description",
            field=wagtail.fields.RichTextField(
                blank=True, null=True, verbose_name="Opis projekta"
            ),
        ),
        migrations.AlterField(
            model_name="projectpage",
            name="duration",
            field=models.TextField(blank=True, verbose_name="Trajanje"),
        ),
        migrations.AlterField(
            model_name="projectpage",
            name="project_owner",
            field=models.TextField(blank=True, verbose_name="Nosilec projekta"),
        ),
        migrations.AlterField(
            model_name="projectpage",
            name="project_value",
            field=models.TextField(blank=True, verbose_name="Trajanje projekta"),
        ),
        migrations.AlterField(
            model_name="projectpage",
            name="results",
            field=models.TextField(blank=True, verbose_name="Uspehi"),
        ),
        migrations.AlterField(
            model_name="projectpage",
            name="website",
            field=models.URLField(
                blank=True, verbose_name="Povezava do spletnega mesta projekta"
            ),
        ),
    ]
