from django.shortcuts import render
# , redirect, get_list_or_404, get_object_or_404
# from melonapi import scrapeMelon

# Create your views here.
def index(request):
    # print(scrapeMelon.getList("LIVE").decode())
    return render(request, 'list.html')