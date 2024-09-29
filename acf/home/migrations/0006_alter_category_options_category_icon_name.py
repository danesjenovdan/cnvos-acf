# Generated by Django 4.2.16 on 2024-09-23 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_category_projecttype_alter_projectpage_contact_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Kategorija", "verbose_name_plural": "Kategorije"},
        ),
        migrations.AddField(
            model_name="category",
            name="icon_name",
            field=models.TextField(blank=True, verbose_name="Ikona"),
        ),
    ]
