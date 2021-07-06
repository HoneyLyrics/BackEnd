from django.urls import path
from . import views

urlpatterns = [
    path('musiclist/', views.MusicList.as_view(), name='musiclist'),
    path('crawler/', views.Crawler.as_view(), name='crawler'),
    path('song/', views.Song.as_view(), name='song')
]