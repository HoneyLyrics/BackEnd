from django.contrib import admin
from .models import SongInfo, Mood, Lyrics

# Register your models here.
class SongInfoAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
    list_display = ['songId', 'title', 'artist', 'mood1', 'mood2', 'mood3', ]
admin.site.register(SongInfo, SongInfoAdmin)

class MoodAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
    list_display = ['moodId', 'mood', ]
admin.site.register(Mood, MoodAdmin)

class LyricsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
    list_display = ['songId', 'content', ]
admin.site.register(Lyrics, LyricsAdmin)
