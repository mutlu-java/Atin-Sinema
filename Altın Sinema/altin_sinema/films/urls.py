
from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),  # Ana sayfa için
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),  # Film detay sayfası için
     path('', views.index, name='index'),  # index.html için
    path('mp2/', views.mp2, name='mp2'),   # mp2.html için
]
