from django.db import models

# Create your models here.
class Mood(models.Model):
    moodId = models.IntegerField(primary_key=True)
    mood = models.CharField(max_length=30)

class SongInfo(models.Model):
    songId = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    imgURL = models.URLField(default='https://cdnimg.melon.co.kr/cm2/album/images/100/43/575/10043575_20210302112520_500.jpg/melon/resize/120/quality/80/optimize')
    mood1 = models.ForeignKey(Mood, related_name='mood1', blank=True, on_delete=models.CASCADE)
    mood2 = models.ForeignKey(Mood, related_name='mood2', blank=True, on_delete=models.CASCADE)
    mood3 = models.ForeignKey(Mood, related_name='mood3', blank=True, on_delete=models.CASCADE)

class Lyrics(models.Model):
    songId = models.ForeignKey(SongInfo, on_delete=models.CASCADE)
    content = models.TextField()