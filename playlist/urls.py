from django.urls import path
from . import views

app_name = "playlist"

urlpatterns = [
    path("", views.playlist_list, name="playlist_list"),
    path("new/", views.playlist_create, name="playlist_create"),
    path("<int:pk>/delete/", views.playlist_delete, name="playlist_delete"),
]
