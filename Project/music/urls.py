from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index', views.index),
    path('genres/', views.genres),
    path('track/', views.track),
    path('add_genre/', views.add_genre),
    path('delete/<int:id_genres>/', views.delete),
    path('edit/<int:id_genres>/', views.edit_genre),
    path('add_track', views.add_track),
    path('delete_track/<int:id_track>/', views.delete_track),
    path('edit_track/<int:id_track>/', views.edit_track),
]
