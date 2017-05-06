from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=250)
    albm_title = models.CharField(max_length=500)
    gener = models.CharField(max_length=100)
    alb_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.albm_title + ' - ' + self.artist


class Song(models.Model):
    albm = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)