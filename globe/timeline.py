"""Лента времени: события из историй городов, отсортированные по годам.

Год определяется по русской подписи события («1789», «14 июля 1789», «753 до н. э.»,
«IX век», «1960-е»), поэтому порядок событий не зависит от языка ответа. События без
распознанного года (например, «Древность и Средневековье») в ленту не попадают.
"""
import re

from .models import DEFAULT_LANG

_ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}
_CENTURY = re.compile(r"\b([IVXLC]+)(?:\s*[–-]\s*[IVXLC]+)?\s*(?:век|века|веков)\b")


def _roman_to_int(value):
    total = 0
    for index, char in enumerate(value):
        number = _ROMAN[char]
        if index + 1 < len(value) and _ROMAN[value[index + 1]] > number:
            total -= number
        else:
            total += number
    return total


def parse_year(label):
    """Приблизительный год по русской подписи события или None, если года нет."""
    label = (label or "").strip()
    if not label:
        return None
    bce = "до н" in label.lower()

    century = _CENTURY.search(label)
    if century:
        number = _roman_to_int(century.group(1))
        # Середина века: «IX век» -> 850, «V век до н. э.» -> -450.
        return -(number * 100 - 50) if bce else (number - 1) * 100 + 50

    numbers = re.findall(r"\d+", label)
    if not numbers:
        return None
    # В «14 июля 1789» год — первое число из 3–4 цифр; иначе берём первое число.
    year = int(next((n for n in numbers if len(n) >= 3), numbers[0]))
    return -year if bce else year


def build_timeline(cities, lang):
    """Список событий {year, label, text, city_id, city, country, country_code}.

    Год берётся из русской истории; подписи и тексты — на языке lang. Если число
    событий в переводе не совпадает с русским (правка в админке), используется русский.
    """
    from .serializers import split_items

    events = []
    for city in cities:
        ru_items = split_items(city.history_ru)
        items = split_items(city.localized("history", lang))
        if len(items) != len(ru_items):
            items = ru_items
        for ru_item, item in zip(ru_items, items):
            year = parse_year(ru_item["label"])
            if year is None:
                continue
            events.append(
                {
                    "year": year,
                    "label": item["label"],
                    "text": item["text"],
                    "city_id": city.id,
                    "city": city.localized("name", lang),
                    "country": city.country.localized("name", lang),
                    "country_code": city.country.code,
                }
            )
    events.sort(key=lambda event: (event["year"], event["city_id"]))
    return events
