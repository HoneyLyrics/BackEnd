from django.contrib import admin
from .models import SongInfo, Mood, Lyrics

# Register your models here.
class SongInfoAdmin(admin.ModelAdmin):
    list_display = ['songId', 'title', 'artist', 'mood1', 'mood2', 'mood3', ]
admin.site.register(SongInfo, SongInfoAdmin)

class MoodAdmin(admin.ModelAdmin):
    list_display = ['mood', ]
admin.site.register(Mood, MoodAdmin)

class LyricsAdmin(admin.ModelAdmin):
    list_display = ['songId', 'content', ]
admin.site.register(Lyrics, LyricsAdmin)
