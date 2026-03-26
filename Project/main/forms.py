from django import forms
from .models import Genres, Track, Artist

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genres
        fields = '__all__'
        labels = {
            'name_ru': 'Название на русском',
            'name_en': 'Название на английском',
            'description': 'Описание',
        }
class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = '__all__'
        labels = {
            'title': 'Название',
            'duration': 'Продолжительность',
            'genres': 'Жанр',
        }

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        labels = {
            'name': 'Имя \ Название',
            'image': 'Изображение',
        }