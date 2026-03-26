from django.db import models

class Genres(models.Model):
    name_ru = models.CharField(max_length = 200, unique = True)
    name_en = models.CharField(max_length = 200)
    description = models.CharField(max_length = 400)
    def __str__(self):
        return self.name_en
    
class Track(models.Model):
    title = models.CharField(max_length = 200, unique = True)
    duration = models.CharField(max_length = 200)
    genre = models.ManyToManyField(Genres)
    def __str__(self):
        return self.title