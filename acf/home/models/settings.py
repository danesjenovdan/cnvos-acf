from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting


@register_setting
class GeneralSettings(BaseGenericSetting):
    financer_disclaimer = models.TextField(blank=True, verbose_name="Disclaimer financerja")

    panels = [
        FieldPanel("financer_disclaimer"),
    ]

    class Meta:
        verbose_name = "Financer"
