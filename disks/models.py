from django.db import models


# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "album"
        # ordering = ['date']

    def __str__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=30)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unitPrice = models.DecimalField()
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    composer = models.CharField(max_length=200)

    def __str__(self):
        return self.name
