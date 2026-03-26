from django import forms
from .models import Genres, Track

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