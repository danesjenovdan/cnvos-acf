# Generated by Django 4.2.16 on 2024-09-23 14:51

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_projectpage_homepage_introduction"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="introduction",
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
    ]
