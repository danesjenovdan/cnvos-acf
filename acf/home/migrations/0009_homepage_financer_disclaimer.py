# Generated by Django 4.2.16 on 2024-09-23 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_projectpage_project_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='financer_disclaimer',
            field=models.TextField(blank=True, verbose_name='Disclaimer financerja'),
        ),
    ]
