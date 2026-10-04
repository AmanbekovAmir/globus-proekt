"""Представления: главная страница и REST API."""
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import City, Country
from .serializers import (
    CityDetailSerializer,
    CityListSerializer,
    CountrySerializer,
    resolve_lang,
)
from .timeline import build_timeline

LANGUAGES = [
    # (код в проекте, короткая подпись, название на самом языке, код для атрибута HTML lang)
    ("ru", "RU", "Русский", "ru"),
    ("uz", "UZ", "Oʻzbekcha", "uz"),
    ("qr", "QR", "Qaraqalpaqsha", "kaa"),  # kaa — ISO 639-3 для каракалпакского
]


def index(request):
    """Главная страница с 3D-глобусом."""
    return render(request, "index.html", {"languages": LANGUAGES})


class LangContextMixin:
    """Передаёт язык из ?lang=ru|uz|qr в сериализатор (по умолчанию ru)."""

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["lang"] = resolve_lang(self.request.query_params.get("lang"))
        return context


class CityListView(LangContextMixin, ListAPIView):
    """GET /api/cities/ — все города: координаты и базовая информация."""

    queryset = City.objects.filter(is_published=True).select_related("country")
    serializer_class = CityListSerializer
    pagination_class = None


class CityDetailView(LangContextMixin, RetrieveAPIView):
    """GET /api/cities/<id>/ — подробности о городе на выбранном языке."""

    queryset = City.objects.filter(is_published=True).select_related("country")
    serializer_class = CityDetailSerializer
    lookup_field = "pk"
    lookup_url_kwarg = "id"


class CountryListView(LangContextMixin, ListAPIView):
    """GET /api/countries/ — страны (добавьте ?boundary=1 для GeoJSON границ)."""

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = None

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["with_boundary"] = self.request.query_params.get("boundary") == "1"
        return context


class TimelineView(APIView):
    """GET /api/timeline/ — события из историй городов по годам (?lang=ru|uz|qr)."""

    def get(self, request):
        lang = resolve_lang(request.query_params.get("lang"))
        cities = City.objects.filter(is_published=True).select_related("country")
        return Response(build_timeline(cities, lang))
