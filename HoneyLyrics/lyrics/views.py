from json.encoder import JSONEncoder
from django.views import View
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render

# , redirect, get_list_or_404, get_object_or_404
# from melonapi import scrapeMelon

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


    


