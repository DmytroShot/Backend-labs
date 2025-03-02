from django.urls import path
from .views import *
urlpatterns = [
    path("",createShortUrl),
    path("<str:shortCode>",getUrl),
    path("<str:shortCode>/update",UpdateShortUrl),
    path("<str:shortCode>/delete",DeleteShortUrl),
    path("<str:shortCode>/stats",ShortUrlStats),
]