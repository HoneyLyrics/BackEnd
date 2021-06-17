from json.encoder import JSONEncoder
from django.views import View
from django.http.response import JsonResponse, HttpResponse
from lyrics.models import SongInfo, Lyrics, Mood
import json
# , redirect, get_list_or_404, get_object_or_404


class Song(View):
    def get(self, request):
        data = []
        if request.GET.get('songid', False):
            song_id = request.GET['songid']
            print("songid", song_id)
            all_entries = SongInfo.objects.filter(songId=song_id)
        for all_entry in all_entries:
            print(all_entry.songId)
            data.append({
                'songId': all_entry.songId,
                'singer': all_entry.artist,
                'imgURL': all_entry.imgURL,
                'title': all_entry.title,
            })
        json_data = json.dumps(data, ensure_ascii=False).encode('utf-8')
        return HttpResponse(json_data, content_type="application/json")


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
                             imageURL=song_info['imgUrl'],
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
        data = []
        if request.GET.get('moodid', False):
            mood = request.GET['moodid']
            all_entries = SongInfo.objects.filter(
                mood1__lte=mood,
                mood2__lte=2,
                mood3__lte=3
            )
            for all_entry in all_entries:
                lyrics = Lyrics.objects.filter(
                         songId=SongInfo.objects.get(songId=all_entry.songId)
                        )[0].content
                data.append({
                    'songId': all_entry.songId,
                    'singer': all_entry.artist,
                    'title': all_entry.title,
                    'imgURL': all_entry.imgURL,
                    'lyrics': lyrics
                })
        json_data = json.dumps(data, ensure_ascii=False).encode('utf-8')
        return HttpResponse(json_data, content_type="application/json")


    # post Data
    def musiclist(self, request):
        return HttpResponse("OK")


    


