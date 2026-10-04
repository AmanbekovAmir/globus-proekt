"""Сериализаторы DRF: данные отдаются сразу на выбранном языке."""
from django.utils.text import Truncator
from rest_framework import serializers

from .models import DEFAULT_LANG, SUPPORTED_LANGS, City, Country


def resolve_lang(value):
    """Приводит значение параметра ?lang= к поддерживаемому языку."""
    return value if value in SUPPORTED_LANGS else DEFAULT_LANG


def split_items(text):
    """Разбирает многострочный текст на элементы {label, text}.

    Строка вида «1966 — Землетрясение…» превращается в
    {"label": "1966", "text": "Землетрясение…"}. Если разделителя « — »
    нет, label остаётся пустым.
    """
    items = []
    for raw in (text or "").splitlines():
        line = raw.strip()
        if not line:
            continue
        label, sep, body = line.partition(" — ")
        if sep and body.strip() and len(label) <= 60:
            items.append({"label": label.strip(), "text": body.strip()})
        else:
            items.append({"label": "", "text": line})
    return items


class LangSerializerMixin:
    @property
    def lang(self):
        return resolve_lang(self.context.get("lang"))


class CountrySerializer(LangSerializerMixin, serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    has_boundary = serializers.SerializerMethodField()

    class Meta:
        model = Country
        fields = ("id", "code", "name", "latitude", "longitude", "has_boundary")

    def get_name(self, obj):
        return obj.localized("name", self.lang)

    def get_has_boundary(self, obj):
        return bool(obj.boundary)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Тяжёлое поле отдаём только по запросу: /api/countries/?boundary=1
        if self.context.get("with_boundary"):
            data["boundary"] = instance.boundary
        return data


class CityListSerializer(LangSerializerMixin, serializers.ModelSerializer):
    """Краткая информация для точек на глобусе."""

    name = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    country_code = serializers.CharField(source="country.code", read_only=True)
    summary = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = (
            "id",
            "name",
            "country",
            "country_code",
            "latitude",
            "longitude",
            "population",
            "is_capital",
            "summary",
        )

    def get_name(self, obj):
        return obj.localized("name", self.lang)

    def get_country(self, obj):
        return obj.country.localized("name", self.lang)

    def get_summary(self, obj):
        return Truncator(obj.localized("description", self.lang)).chars(140)


class CityDetailSerializer(CityListSerializer):
    """Полная информация о городе для боковой панели."""

    lang = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    history = serializers.SerializerMethodField()
    industry = serializers.SerializerMethodField()

    class Meta(CityListSerializer.Meta):
        fields = (
            "id",
            "lang",
            "name",
            "country",
            "country_code",
            "latitude",
            "longitude",
            "population",
            "is_capital",
            "description",
            "history",
            "industry",
        )

    def get_lang(self, obj):
        return resolve_lang(self.context.get("lang"))

    def get_description(self, obj):
        return obj.localized("description", resolve_lang(self.context.get("lang")))

    def get_history(self, obj):
        return split_items(obj.localized("history", resolve_lang(self.context.get("lang"))))

    def get_industry(self, obj):
        return split_items(obj.localized("industry", resolve_lang(self.context.get("lang"))))
