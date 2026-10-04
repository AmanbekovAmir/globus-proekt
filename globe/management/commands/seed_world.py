"""Добавляет в базу известные города мира (ru/uz/qr).

    python manage.py seed_world            # только недостающее, ничего не перезаписывает
    python manage.py seed_world --update   # дополнительно перезаписать тексты этих городов
    python manage.py seed_world --dry-run  # показать, что будет добавлено

Команда идемпотентна: страны ищутся по коду, города — по паре (страна, название ru).
Правки, сделанные в админке, без --update не затрагиваются.
"""
from django.core.management.base import BaseCommand
from django.db import transaction

from globe.models import City, Country
from globe.seed_data import CITIES, COUNTRIES


def city_fields(data):
    name_ru, name_uz, name_qr = data["name"]
    fields = {
        "name_uz": name_uz,
        "name_qr": name_qr,
        "latitude": data["lat"],
        "longitude": data["lng"],
        "population": data["population"],
        "is_capital": data["capital"],
        "is_published": True,
    }
    for i, lang in enumerate(("ru", "uz", "qr")):
        fields[f"description_{lang}"] = data["desc"][i]
        fields[f"history_{lang}"] = "\n".join(data["history"][i])
        fields[f"industry_{lang}"] = "\n".join(data["industry"][i])
    return fields


class Command(BaseCommand):
    help = "Добавляет известные города и страны (ru/uz/qr) без дублей."

    def add_arguments(self, parser):
        parser.add_argument("--update", action="store_true", help="Перезаписать уже существующие города из набора.")
        parser.add_argument("--dry-run", action="store_true", help="Ничего не сохранять, только показать план.")

    @transaction.atomic
    def handle(self, *args, **options):
        update, dry = options["update"], options["dry_run"]
        countries, created_c, created_ct, updated_ct, skipped = {}, 0, 0, 0, 0

        needed = {c["country"] for c in CITIES}
        for code in sorted(needed):
            name_ru, name_uz, name_qr, lat, lng = COUNTRIES[code]
            country = Country.objects.filter(code=code).first()
            if country is None:
                created_c += 1
                self.stdout.write(f"+ страна {code}: {name_ru}")
                country = Country(
                    code=code, name_ru=name_ru, name_uz=name_uz, name_qr=name_qr,
                    latitude=lat, longitude=lng,
                )
                if not dry:
                    country.save()
            countries[code] = country

        for data in CITIES:
            country = countries[data["country"]]
            name_ru = data["name"][0]
            existing = (
                City.objects.filter(country=country, name_ru=name_ru).first()
                if country.pk else None
            )
            if existing is None:
                created_ct += 1
                self.stdout.write(f"+ город {name_ru} ({country.code})")
                if not dry:
                    City.objects.create(country=country, name_ru=name_ru, **city_fields(data))
            elif update:
                updated_ct += 1
                self.stdout.write(f"~ обновлён {name_ru}")
                if not dry:
                    for key, value in city_fields(data).items():
                        setattr(existing, key, value)
                    existing.save()
            else:
                skipped += 1
                self.stdout.write(f"= уже есть: {name_ru}")

        prefix = "[dry-run] " if dry else ""
        self.stdout.write(self.style.SUCCESS(
            f"{prefix}Стран добавлено: {created_c}; городов добавлено: {created_ct}, "
            f"обновлено: {updated_ct}, пропущено (уже есть): {skipped}."
        ))
