from django.contrib import admin

from .models import City, Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name_ru", "name_uz", "name_qr", "code")
    search_fields = ("name_ru", "name_uz", "name_qr", "code")


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name_ru", "name_uz", "name_qr", "country", "population", "is_capital", "is_published")
    list_filter = ("country", "is_capital", "is_published")
    search_fields = ("name_ru", "name_uz", "name_qr")
    fieldsets = (
        (None, {"fields": ("country", ("latitude", "longitude"), "population", ("is_capital", "is_published"))}),
        ("Русский (ru)", {"fields": ("name_ru", "description_ru", "history_ru", "industry_ru")}),
        ("Oʻzbekcha (uz)", {"fields": ("name_uz", "description_uz", "history_uz", "industry_uz")}),
        ("Qaraqalpaqsha (qr)", {"fields": ("name_qr", "description_qr", "history_qr", "industry_qr")}),
    )
