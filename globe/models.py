"""Модели данных: страны и города с контентом на трёх языках (ru, uz, qr)."""
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

SUPPORTED_LANGS = ("ru", "uz", "qr")
DEFAULT_LANG = "ru"

LAT_VALIDATORS = [MinValueValidator(-90), MaxValueValidator(90)]
LNG_VALIDATORS = [MinValueValidator(-180), MaxValueValidator(180)]


class LocalizedMixin:
    """Возвращает значение поля на нужном языке.

    Если перевод не заполнен, используется русский вариант.
    """

    def localized(self, field, lang=DEFAULT_LANG):
        if lang not in SUPPORTED_LANGS:
            lang = DEFAULT_LANG
        value = getattr(self, f"{field}_{lang}", "")
        return value or getattr(self, f"{field}_{DEFAULT_LANG}", "")


class Country(LocalizedMixin, models.Model):
    code = models.CharField(
        "Код страны (ISO 3166-1 alpha-2)",
        max_length=2,
        unique=True,
        help_text="Например: UZ, RU, JP, US. По этому коду на глобусе подсвечиваются границы.",
    )
    name_ru = models.CharField("Название (ru)", max_length=200)
    name_uz = models.CharField("Название (uz)", max_length=200, blank=True)
    name_qr = models.CharField("Название (qr)", max_length=200, blank=True)

    latitude = models.FloatField("Широта центра", validators=LAT_VALIDATORS)
    longitude = models.FloatField("Долгота центра", validators=LNG_VALIDATORS)
    boundary = models.JSONField(
        "Границы (GeoJSON geometry)",
        null=True,
        blank=True,
        help_text="Необязательно. Polygon или MultiPolygon в формате GeoJSON.",
    )

    class Meta:
        verbose_name = "страна"
        verbose_name_plural = "страны"
        ordering = ["name_ru"]

    def __str__(self):
        return f"{self.name_ru} ({self.code})"


class City(LocalizedMixin, models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="cities",
        verbose_name="Страна",
    )

    name_ru = models.CharField("Название (ru)", max_length=200)
    name_uz = models.CharField("Название (uz)", max_length=200, blank=True)
    name_qr = models.CharField("Название (qr)", max_length=200, blank=True)

    latitude = models.FloatField("Широта", validators=LAT_VALIDATORS)
    longitude = models.FloatField("Долгота", validators=LNG_VALIDATORS)
    population = models.PositiveIntegerField("Население (приблизительно)", null=True, blank=True)
    is_capital = models.BooleanField("Столица государства", default=False)
    is_published = models.BooleanField("Показывать на глобусе", default=True)

    description_ru = models.TextField("Описание (ru)", blank=True)
    description_uz = models.TextField("Описание (uz)", blank=True)
    description_qr = models.TextField("Описание (qr)", blank=True)

    history_ru = models.TextField(
        "История (ru)",
        blank=True,
        help_text="Одно событие на строку в формате «Год — событие».",
    )
    history_uz = models.TextField("История (uz)", blank=True, help_text="Формат: «Год — событие».")
    history_qr = models.TextField("История (qr)", blank=True, help_text="Формат: «Год — событие».")

    industry_ru = models.TextField(
        "Компании и производство (ru)",
        blank=True,
        help_text="Одна позиция на строку в формате «Название — описание».",
    )
    industry_uz = models.TextField(
        "Компании и производство (uz)", blank=True, help_text="Формат: «Название — описание»."
    )
    industry_qr = models.TextField(
        "Компании и производство (qr)", blank=True, help_text="Формат: «Название — описание»."
    )

    class Meta:
        verbose_name = "город"
        verbose_name_plural = "города"
        ordering = ["name_ru"]

    def __str__(self):
        return self.name_ru
