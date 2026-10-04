"""Маршруты приложения: страница и API."""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/cities/", views.CityListView.as_view(), name="city-list"),
    path("api/cities/<int:id>/", views.CityDetailView.as_view(), name="city-detail"),
    path("api/countries/", views.CountryListView.as_view(), name="country-list"),
    path("api/timeline/", views.TimelineView.as_view(), name="timeline"),
]
