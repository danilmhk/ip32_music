from django.shortcuts import render, redirect
from .forms import GenreForm, TrackForm, ArtistForm
from .models import Genres, Track, Artist
from django.http import HttpResponseRedirect, HttpResponse

def index (request):
    genres1 = Genres.objects.all()
    return render (request, 'index.html', {'genres1': genres1})

def genres (request):
    genres1 = Genres.objects.all()
    return render (request, 'genres.html', {'genres1': genres1})

def track(request):
    tracks = Track.objects.all()
    artists = Artist.objects.all()
    artist = None
    
    if request.method == "POST":
        id_artist = request.POST.get('artist')
        if id_artist:
            artist = Artist.objects.get(id=id_artist)
            tracks = Track.objects.filter(artist=artist)
    
    return render(request, 'track.html', {
        'track1': tracks,
        'artists': artists,
        'current_artist': artist
    })
    

def delete(request, id_genres):
    genres = Genres.objects.get(id=id_genres)
    genres.delete()
    return HttpResponse("<h1>Успешно удалено</h1><br><a href='/'>На главную</a>")

def add_genre(request):
    if request.method == "POST":
        genres_form = GenreForm(request.POST)
        if genres_form.is_valid():
            genres_form.save()
            return redirect('/genres')
    else:
        genres_form = GenreForm()
    return render(request, "add_genre.html", {'form': genres_form})

def edit_genre(request, id_genres):
    g = Genres.objects.get(id=id_genres)
    if request.method == "POST":
        genre = GenreForm(request.POST, instance=g)
        if genre.is_valid():
            genre.save()
            return redirect('/genres')
    else:
        genreform = GenreForm(instance=g)
        return render(request, "edit_genre.html", {"form": genreform})
    
def add_track(request):
    if request.method == "POST":
        track = TrackForm(request.POST)
        if track.is_valid():
            track.save()
            return redirect('/track/')
    else:
        form = TrackForm()
    return render(request, "add_track.html", {"form": form})

def delete_track(request, id_track):
    track_item = Track.objects.get(id=id_track)
    track_item.delete()
    return HttpResponse("<h1>Успешно удалено</h1><br><a href='/'>На главную</a>")

def edit_track(request, id_track):
    t = Track.objects.get(id=id_track)
    if request.method == "POST":
        form = TrackForm(request.POST, instance=t)
        if form.is_valid():
            form.save()
            return redirect('/track/')
    else:
        form = TrackForm(instance=t)
    return render(request, "edit_track.html", {"form": form})

def artists(request):
    a = Artist.objects.all()
    return render(request, 'artists.html', {'artists': a})

def add_artist(request):
    if request.method == "POST":
        artists_form = ArtistForm(request.POST, request.FILES)
        if artists_form.is_valid():
            artists_form.save()
            return redirect('artists/')
    else:
        artists_form = ArtistForm()
    return render(request, "add_artist.html", {'form': artists_form})

# def trackList(request):
#     tracks = Track.objects.all()
#     artists = Artist.objects.all()
#     artist = None
#     if request.method == "POST":
#          id_artist = request.POST.get('artist')
#          artist = Artist.objects.get(id=id_artist)
#          tracks = Track.objects.filter(artist=artist)
#     return render(request, 'tracks.html', {'tracks': tracks, 'artists': artists, 'current_artist': artist})