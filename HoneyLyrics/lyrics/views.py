from json.encoder import JSONEncoder
from django.views import View
from django.http.response import JsonResponse, HttpResponse
from lyrics.models import SongInfo, Lyrics, Mood
import json
# , redirect, get_list_or_404, get_object_or_404

class Crawler(View):
    def get(self, request):
        pass

    def post(self, request):
        data = json.loads(request.body)
        # TODO Data predict code 넣기
        for song_info in data:
            song = SongInfo(songId=song_info['songId'], 
                             title=song_info['title'],
                             artist=song_info['artists'],
                             mood1 = Mood.objects.get(moodId=1),
                             mood2 = Mood.objects.get(moodId=2),
                             mood3 = Mood.objects.get(moodId=3))

            lyric = Lyrics(songId=SongInfo.objects.get(songId=song_info['songId']), 
                           content=song_info['lyrics'])
            song.save()
            lyric.save()

        return HttpResponse("OK")

# Create your views here.

class MusicList(View):

    # GET Data
    def get(self, request):
        if request.GET('moodid', False):
            print(request.GET['moodid'])
        return JsonResponse({"1":"1"})

    # post Data
    def musiclist(self, request):
        return HttpResponse("OK")


    


