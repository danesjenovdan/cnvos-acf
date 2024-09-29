from django.db import models
from django import forms

from wagtail import blocks
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.images.blocks import ImageChooserBlock


@register_snippet
class Category(models.Model):
    name = models.TextField(blank=True, verbose_name="Ime kategorije")
    icon = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Ikona",
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("icon"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategorija"
        verbose_name_plural = "Kategorije"


@register_snippet
class ProjectType(models.Model):
    name = models.TextField(blank=True, verbose_name="Tip projekta")
    icon = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Ikona",
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("icon"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tip projekta"
        verbose_name_plural = "Tipi projektov"


class ProjectsFilterForm(forms.Form):
    kategorija = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Category.objects,
        widget=forms.CheckboxSelectMultiple(attrs={"class": ""}),
    )
    tip_projekta = forms.ModelMultipleChoiceField(
        required=False,
        queryset=ProjectType.objects,
        widget=forms.CheckboxSelectMultiple(attrs={"class": ""}),
    )


class HomePage(Page):
    introduction = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
    ]

    parent_page_type = []
    subpage_types = [
        "home.ProjectPage",
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # prepare for filters
        categories = Category.objects.all().order_by("id")
        project_types = ProjectType.objects.all().order_by("id")

        # get projects
        projects = ProjectPage.objects.all()

        # filtering
        form = ProjectsFilterForm(request.GET)
        if form.is_valid():
            categories_filter = form.cleaned_data["kategorija"]
            if categories_filter:
                projects = projects.filter(category__in=categories_filter)
            project_types_filter = form.cleaned_data["tip_projekta"]
            if project_types_filter:
                projects = projects.filter(project_type__in=project_types_filter)

        categories_dict = {}

        for category in categories:
            category_projects = projects.filter(category=category)
            categories_dict[category.id] = {
                "projects": category_projects,
                "category": category,
            }

        return {
            **context,
            "categories": categories,
            "project_types": project_types,
            "projects": categories_dict,
            "form": form,
        }


class ProjectPage(Page):
    project_owner = models.TextField(blank=True, verbose_name="Nosilec projekta")
    card_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Slika na kartici",
    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Kategorija",
    )
    project_type = models.ForeignKey(
        ProjectType,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Tip projekta",
    )
    description = RichTextField(blank=True, null=True, verbose_name="Opis projekta")
    budget = models.TextField(blank=True)
    duration = models.TextField(blank=True, verbose_name="Trajanje")
    results = models.TextField(blank=True, verbose_name="Uspehi")
    photos = StreamField(
        [
            ("image", ImageChooserBlock(label="Slika")),
        ],
        verbose_name="Slike",
        null=True,
        blank=True,
    )
    website = models.URLField(
        blank=True, verbose_name="Povezava do spletnega mesta projekta"
    )
    contact_person = models.TextField(blank=True, verbose_name="Vodja projekta")
    contact = models.EmailField(blank=True, verbose_name="Kontakt vodje projekta")

    content_panels = Page.content_panels + [
        FieldPanel("category"),
        FieldPanel("project_type"),
        MultiFieldPanel(
            [
                FieldPanel("project_owner"),
                FieldPanel("card_image"),
            ],
            heading="Osnovni podatki",
        ),
        FieldPanel("description"),
        FieldPanel("photos"),
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
                FieldPanel("contact_person"),
                FieldPanel("contact"),
            ],
            heading="Kontakt",
        ),
    ]

    parent_page_type = ["home.HomePage"]
    subpage_types = []
