import pandas as pd
import requests
import re
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from time import sleep
import random

URL = {
    'LIVE': 'https://www.melon.com/chart/index.htm',
    'RISE': 'https://www.melon.com/chart/rise/index.htm',
    'DAY': 'https://www.melon.com/chart/day/index.htm',
    'WEEK': 'https://www.melon.com/chart/week/index.htm',
    'MONTH': 'https://www.melon.com/chart/month/index.htm'
}

def getList(time):
    """Generates json file of the top 100 songs + (additional metadata) on Melon

    Args:
        time (str): Which chart you want (LIVE, RISE, DAY, WEEK, MONTH)

    Returns:
        json (str): Seralized json string that contains the top 100 songs. 
                    Key is ranking of song; value is name, ranking, artists, songId, albumId (id's are Melon specific).  
					NOTE: You want to use json.loads(getList("time")) to deseralize the data. 

    """
    html = requests.get(URL[time.upper()], headers={'User-Agent':"github.com/ko28/melon-api"}).text
    soup = BeautifulSoup(html, "lxml")
    data = {}
    # Melon recently changed how their live chart works, tried to fix it as best as I could
    if time.upper() == "LIVE":
        rank = 1
        for tag in soup.findAll("tr", {"data-song-no": True}):
            # Key is ranking of the song
            data[rank] = {
                "name": tag.find("div", {"class": "ellipsis rank01"}).getText().strip(),
                "artists": tag.find("span", {"class": "checkEllipsis"}).getText(),
                "ranking": rank,
                "songId": re.search(r'goSongDetail\(\'([0-9]+)\'\)', str(tag)).group(1)
            }
            rank += 1

    else:
        for tag in soup.findAll("tr", {"class": ["lst50", "lst100"]}):
            # Key is ranking of the song
            data[tag.find("span", {"class": ["rank top", "rank"]}).getText()] = {
                "title": tag.find("div", {"class": "ellipsis rank01"}).getText().strip(),
                "ranking": tag.find("span", {"class": ["rank top", "rank"]}).getText(),
                "artists": tag.find("span", {"class": "checkEllipsis"}).getText(),
                "songId": re.search(r'goSongDetail\(\'([0-9]+)\'\)', str(tag)).group(1)
            }      
    return data

# songId로부터 가사를 가지고 오는 코드
def getLyric(songId):
    url = 'https://www.melon.com/song/detail.htm?songId=' + str(songId)
    req = requests.get(url, headers={'User-Agent':"github.com/ko28/melon-api"})
    html = req.text.replace("<BR>", "\n")
    soup = BeautifulSoup(html, "lxml")
    lyrics = soup.find("div", {"class": "lyric"})
    return lyrics.text.strip() 

# 크롤링한 결과(30일 인기차트 노래 100개)를 가져와서 data에 저장하는 코드
def parsing_info():
    data = []
    for _, song_info in getList("MONTH").items():
        sleep(random.randint(3, 10))
        url = "https://www.melon.com/song/detail.htm?songId=" + str(song_info["songId"])
        html = Request(url, headers={'User-Agent': 'Mozilla/5.0'})       # Header의 속성에 Header Information을 넣어둠
        soup = BeautifulSoup(urlopen(html).read(), "html.parser")
        thumb = soup.find("div", {"class": "thumb"})
        imgurl = thumb.find('img')['src']
        # print(song_info["title"], imgurl)     # 이미지 url 잘 나오는지 출력
        data.append(
            {
            "songId":song_info["songId"],
            "title": song_info["title"],
            "artists": song_info["artists"],
            "imgUrl": imgurl,
            "lyrics": getLyric(int(song_info["songId"]))
            }
        )
    return data

# csv 저장하는 함수
def write_csv():
    data = parsing_info()
    df = pd.DataFrame.from_dict(data)
    df.to_csv('./data/result.csv', index=False)
    return data

def main():
    write_csv()

if __name__ == "__main__":
    main()