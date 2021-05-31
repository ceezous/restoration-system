from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('oldphotorestoration/', views.oldPhotoRestoration),
    path('deraindrop/', views.deRainDrop),
    path('derain/', views.deRain),
    path('dehaze/', views.deHaze),
]