from django.db import models

class Genres(models.Model):
    name_ru = models.CharField(max_length = 200, unique = True)
    name_en = models.CharField(max_length = 200)
    description = models.CharField(max_length = 400)
    def __str__(self):
        return self.name_en
    

class Artist(models.Model):
    name = models.CharField(max_length=500, unique = True)
    image = models.ImageField(upload_to='artists/', null=True)
    def __str__(self):
        return self.name 
    
class Track(models.Model):
    title = models.CharField(max_length = 200, unique = True)
    duration = models.CharField(max_length = 200)
    genre = models.ManyToManyField(Genres)
    artist = models.ForeignKey(Artist, on_delete=models.RESTRICT, null=True)
    def __str__(self):
        return self.title
