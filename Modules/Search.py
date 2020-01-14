import bs4
import lxml
import discord
from urllib.request import urlopen, Request
import urllib
import json
import requests
import random
class Search:
    def get_video_link(self, titleli):
        return
        
    def search_image(self, titleli):
        title = ''
        for i in titleli:
            title = title + " " + i
        enc_location = urllib.parse.quote(title)
        hdr = {'User-Agent': 'Mozilla/5.0'}
        #url = 'https://imgur.com/search/score?q='+enc_location
        url = 'https://www.google.co.kr/search?hl=en&tbm=isch&q=' + enc_location
        #디버깅용 코드. 
        #print(url)
        #print(titleli)
        #print(title)
        #print(enc_location)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html,"lxml")
        embed = discord.Embed(colour = 0xb4151c)
        imgdinfl = bsObj.find_all("img")
        #print(imgdinfl)
        try:
            randomNum = random.randint(0,(len(imgdinfl) - 1)/2)
            imgsrc = imgdinfl[randomNum].get('src')
            embed.set_image(url=imgsrc)
            print(imgsrc)
        except ValueError:
            embed.add_field(name="검색된 사진이 없음...",value = "사진이 없습니다.")
        return embed

