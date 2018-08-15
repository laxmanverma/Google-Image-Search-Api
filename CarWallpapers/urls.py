from django.urls import path

from CarWallpapers.src.Controller import WallpaperController

urlpatterns = [
    path('googleSearch', WallpaperController.googleSearch, name='googleSearch'),
]