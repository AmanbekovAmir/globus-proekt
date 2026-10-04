from io import StringIO

from django.core.management import call_command
from django.test import TestCase

from .models import City, Country
from .seed_data import CITIES


class SeedWorldTests(TestCase):
    def run_seed(self, *args):
        out = StringIO()
        call_command("seed_world", *args, stdout=out)
        return out.getvalue()

    def test_creates_cities_with_all_languages(self):
        self.run_seed()
        self.assertEqual(City.objects.count(), len(CITIES))
        for city in City.objects.all():
            for lang in ("ru", "uz", "qr"):
                self.assertTrue(getattr(city, f"name_{lang}"), city)
                self.assertTrue(getattr(city, f"description_{lang}"), city)
                self.assertTrue(getattr(city, f"history_{lang}"), city)
                self.assertTrue(getattr(city, f"industry_{lang}"), city)

    def test_is_idempotent_and_keeps_admin_edits(self):
        self.run_seed()
        paris = City.objects.get(name_ru="Париж")
        paris.description_ru = "Правка из админки"
        paris.save()
        countries = Country.objects.count()

        self.run_seed()
        self.assertEqual(City.objects.count(), len(CITIES))
        self.assertEqual(Country.objects.count(), countries)
        paris.refresh_from_db()
        self.assertEqual(paris.description_ru, "Правка из админки")

        self.run_seed("--update")
        paris.refresh_from_db()
        self.assertNotEqual(paris.description_ru, "Правка из админки")

    def test_dry_run_saves_nothing(self):
        self.run_seed("--dry-run")
        self.assertEqual(City.objects.count(), 0)
        self.assertEqual(Country.objects.count(), 0)

    def test_api_returns_new_cities(self):
        self.run_seed()
        response = self.client.get("/api/cities/?lang=qr")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), len(CITIES))


class SeedDataTests(TestCase):
    def test_seed_data_is_consistent(self):
        from .seed_data import COUNTRIES

        for data in CITIES:
            self.assertIn(data["country"], COUNTRIES, data["name"][0])
            for part in ("name", "desc", "history", "industry"):
                self.assertEqual(len(data[part]), 3, (data["name"][0], part))
            for lang_index in range(3):
                self.assertTrue(data["desc"][lang_index], data["name"][0])
                self.assertTrue(data["history"][lang_index], data["name"][0])
                self.assertTrue(data["industry"][lang_index], data["name"][0])
            self.assertEqual(
                {len(items) for items in data["history"]}, {len(data["history"][0])}, data["name"][0]
            )


class TimelineTests(TestCase):
    def test_parse_year(self):
        from .timeline import parse_year

        cases = {
            "1789": 1789,
            "14 июля 1789": 1789,
            "753 до н. э.": -753,
            "Около 10 г. до н. э.": -10,
            "IX век": 850,
            "IX–X века": 850,
            "1960-е": 1960,
            "1814–1815": 1814,
            "Древность и Средневековье": None,
            "": None,
        }
        for label, year in cases.items():
            self.assertEqual(parse_year(label), year, label)

    def test_timeline_api_is_sorted_and_consistent_across_languages(self):
        call_command("seed_world", stdout=StringIO())
        results = {}
        for lang in ("ru", "uz", "qr"):
            response = self.client.get(f"/api/timeline/?lang={lang}")
            self.assertEqual(response.status_code, 200)
            events = response.json()
            self.assertTrue(events)
            years = [event["year"] for event in events]
            self.assertEqual(years, sorted(years))
            for event in events:
                self.assertTrue(event["label"] and event["text"] and event["city"], event)
            results[lang] = [(event["year"], event["city_id"]) for event in events]
        self.assertEqual(results["ru"], results["uz"])
        self.assertEqual(results["ru"], results["qr"])
