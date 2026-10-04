"""Начальные данные для команды `python manage.py seed_world`.

Страны (в том числе 4 из исходной фикстуры) и города с описанием на ru/uz/qr.
"""
from . import americas_oceania, asia, europe, extra, more, uzbekistan

# code: (name_ru, name_uz, name_qr, широта центра, долгота центра)
COUNTRIES = {
    "UZ": ("Узбекистан", "Oʻzbekiston", "Ózbekstan", 41.3775, 64.5853),
    "RU": ("Россия", "Rossiya", "Rossiya", 61.5240, 105.3188),
    "JP": ("Япония", "Yaponiya", "Yaponiya", 36.2048, 138.2529),
    "US": ("США", "Amerika Qoʻshma Shtatlari", "Amerika Qurama Shtatları", 37.0902, -95.7129),
    "FR": ("Франция", "Fransiya", "Franciya", 46.6, 2.5),
    "GB": ("Великобритания", "Buyuk Britaniya", "Ullı Britaniya", 54.0, -2.5),
    "DE": ("Германия", "Germaniya", "Germaniya", 51.2, 10.4),
    "IT": ("Италия", "Italiya", "Italiya", 42.8, 12.6),
    "TR": ("Турция", "Turkiya", "Túrkiya", 39.0, 35.2),
    "EG": ("Египет", "Misr", "Mısır", 26.8, 30.8),
    "CN": ("Китай", "Xitoy", "Qıtay", 35.0, 103.8),
    "IN": ("Индия", "Hindiston", "Hindstan", 22.0, 79.0),
    "KR": ("Южная Корея", "Janubiy Koreya", "Qubla Koreya", 36.5, 127.9),
    "AE": ("ОАЭ", "Birlashgan Arab Amirliklari", "Birlesken Arab Ámirlikleri", 24.0, 54.0),
    "KZ": ("Казахстан", "Qozogʻiston", "Qazaqstan", 48.0, 67.0),
    "AU": ("Австралия", "Avstraliya", "Avstraliya", -25.7, 134.5),
    "BR": ("Бразилия", "Braziliya", "Braziliya", -10.8, -52.9),
    "MX": ("Мексика", "Meksika", "Meksika", 23.6, -102.5),
    "KG": ("Кыргызстан", "Qirgʻiziston", "Qırǵızstan", 41.2, 74.8),
    "TJ": ("Таджикистан", "Tojikiston", "Tájikstan", 38.9, 71.3),
    "TM": ("Туркменистан", "Turkmaniston", "Túrkmenstan", 39.0, 59.6),
    "AZ": ("Азербайджан", "Ozarbayjon", "Ázerbayjan", 40.3, 47.7),
    "ES": ("Испания", "Ispaniya", "Ispaniya", 40.2, -3.7),
    "CA": ("Канада", "Kanada", "Kanada", 56.1, -106.3),
    "AR": ("Аргентина", "Argentina", "Argentina", -38.4, -63.6),
    "ZA": ("ЮАР", "Janubiy Afrika Respublikasi", "Qubla Afrika Respublikası", -29.0, 24.7),
    "SA": ("Саудовская Аравия", "Saudiya Arabistoni", "Saudiya Arabstanı", 24.0, 45.0),
    "TH": ("Таиланд", "Tailand", "Tailand", 15.0, 101.0),
    "ID": ("Индонезия", "Indoneziya", "Indoneziya", -2.5, 118.0),
}

COUNTRIES.update(extra.COUNTRIES)

CITIES = europe.CITIES + asia.CITIES + americas_oceania.CITIES + more.CITIES + extra.CITIES + uzbekistan.CITIES
