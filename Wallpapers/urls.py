from django.urls import path

from Wallpapers.src.Controller import WallpaperController

urlpatterns = [
    path('googleSearch', WallpaperController.googleSearch, name='googleSearch'),
]