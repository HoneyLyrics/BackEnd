from django.views import View
from django.http.response import HttpResponse
from lyrics.models import SongInfo, Lyrics, Mood
import json
from django.db.models import Q


class Song(View):
    """ Create SongInfo by GET method

        returns:
            HttpResponse
    """
    def get(self, request):
        data = []
        if request.GET.get('songid', False):
            song_id = request.GET['songid']
            all_entries = SongInfo.objects.filter(songId=song_id)
            for all_entry in all_entries:
                data.append({
                    'songId': all_entry.songId,
                    'singer': all_entry.artist,
                    'imgURL': all_entry.imgURL,
                    'title': all_entry.title,
                    'mood1': all_entry.mood1.moodId,
                    'mood2': all_entry.mood2.moodId,
                    'mood3': all_entry.mood3.moodId, 
                })
        json_data = json.dumps(data, ensure_ascii=False).encode('utf-8')
        return HttpResponse(json_data, content_type="application/json")


class Crawler(View):
    """ Get data from Models

        returns:
            HttpResponse
    """
    def post(self, request):
        data = json.loads(request.body)
        # TODO Data predict code 넣기
        for song_info in data:
            song = SongInfo(songId=song_info['songId'],
                            title=song_info['title'],
                            artist=song_info['artists'],
                            imgURL=song_info['imgUrl'],
                            mood1=Mood.objects.get(moodId=song_info['mood1']),
                            mood2=Mood.objects.get(moodId=song_info['mood2']),
                            mood3=Mood.objects.get(moodId=song_info['mood3'])
                            )
            lyric = Lyrics(songId=SongInfo.objects.get(songId=song_info['songId']), 
                           content=song_info['lyrics'])
            song.save()
            lyric.save()
        return HttpResponse("OK")


class MusicList(View):
    """ Create MusicList by GET method

        returns:
            HttpResponse
    """
    def get(self, request):
        data = []
        if request.GET.get('moodid', False):
            mood = request.GET['moodid']
            all_entries = SongInfo.objects.filter(
                Q(mood1=Mood.objects.get(moodId=mood))|
                Q(mood2=Mood.objects.get(moodId=mood))|
                Q(mood3=Mood.objects.get(moodId=mood))
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


    def musiclist(self, request):
        return HttpResponse("OK")