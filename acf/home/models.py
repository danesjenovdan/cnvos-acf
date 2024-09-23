from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class Category(models.Model):
    name = models.TextField(blank=True, verbose_name="Ime kategorije")
    icon_name = models.TextField(blank=True, verbose_name="Ikona")

    panels = [
        FieldPanel("name"),
        FieldPanel("icon_name"),
    ]

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Kategorija"
        verbose_name_plural = "Kategorije"


@register_snippet
class ProjectType(models.Model):
    name = models.TextField(blank=True, verbose_name="Tip projekta")

    panels = [
        FieldPanel("name"),
    ]

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Tip projekta"
        verbose_name_plural = "Tipi projektov"


class HomePage(Page):
    introduction = RichTextField(blank=True, null=True)
    financer_disclaimer = models.TextField(blank=True, verbose_name="Disclaimer financerja")

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("financer_disclaimer"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        projects = ProjectPage.objects.all()

        categories = Category.objects.all().order_by("id")

        categories_dict = {}

        for category in categories:
            category_projects = projects.filter(category=category)
            categories_dict[category.name] = category_projects

        return {
            **context,
            "projects": projects,
            "categories": categories_dict,
        }


class ProjectPage(Page):
    project_owner = models.TextField(blank=True, verbose_name="Nosilec projekta")
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Kategorija",)
    project_type = models.ForeignKey(
        ProjectType,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Tip projekta",)
    description = RichTextField(blank=True, null=True, verbose_name="Opis projekta")
    budget = models.TextField(blank=True)
    duration = models.TextField(blank=True, verbose_name="Trajanje")
    results = models.TextField(blank=True, verbose_name="Uspehi")
    # photos
    website = models.URLField(blank=True, verbose_name="Povezava do spletnega mesta projekta")
    contact = models.TextField(blank=True, verbose_name="Kontakt vodje projekta")

    content_panels = Page.content_panels + [
        FieldPanel("category"),
        FieldPanel("project_type"),
        MultiFieldPanel(
            [
                FieldPanel("project_owner"),
            ],
            heading="Osnovni podatki",
        ),
        FieldPanel("description"),
        MultiFieldPanel(
            [
                FieldPanel("budget"),
                FieldPanel("duration"),
                FieldPanel("results"),
            ],
            heading="Grafike",
        ),
        MultiFieldPanel(
            [
                FieldPanel("website"),
                FieldPanel("contact"),
            ],
            heading="Kontakt",
        ),
    ]


