from django.contrib import admin
from .models import Genres
from .models import Track
# Register your models here.
admin.site.register(Genres)
admin.site.register(Track)