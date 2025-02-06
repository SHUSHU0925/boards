from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Playlist
from .forms import PlaylistForm


class HomeView(TemplateView):
    template_name = "index.html"
    extra_context = {"message": "Welcome to the Home Page!"}


def playlist_list(request):
    playlists = Playlist.objects.all()
    form = PlaylistForm()
    return render(
        request, "playlist/playlist_list.html", {"playlists": playlists, "form": form}
    )


def playlist_create(request):
    if request.method == "POST":
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.save()
            return redirect("playlist:playlist_list")
    else:
        form = PlaylistForm()
    return render(request, "playlist/playlist_list.html", {"form": form})


def playlist_delete(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk)
    playlist.delete()
    return redirect("playlist:playlist_list")


def get(request):
    playlist_title = "title"
    params = {"playlist_title": playlist_title}
    return render(request, "playlist/index.html", params)
