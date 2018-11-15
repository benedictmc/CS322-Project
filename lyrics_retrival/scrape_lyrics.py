from bs4 import BeautifulSoup
import urllib.request
import json
import os
from itertools import chain
import argparse
import sys
import compile_lyrics


class ScapeLyrics():
    
    ACESS_TOKEN = '6REGZk9IyfkJOrmZddVX39nMlSXYRm6a087_b9pYz0GA30nj7V52Tdxc2WfpDSw1'
    HEADER = { 'User-Agent': 'CompuServe Classic/1.22',
                'Accept': 'application/json',
                'Host': 'api.genius.com',
                'Authorization': 'Bearer 6REGZk9IyfkJOrmZddVX39nMlSXYRm6a087_b9pYz0GA30nj7V52Tdxc2WfpDSw1' }

    def __init__(self, artist):
        self.hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
        artist_f = artist.replace(' ', '_')
        self.song_dict, self.url_list = {}, []
        self.artist_id = self.get_artist_id(artist)

        if os.path.exists(f'meta/{artist_f}_url_list.json'):
            with open(f'meta/{artist_f}_url_list.json') as f:
                self.url_list = json.load(f)
        else:
            self.get_url_list(self.artist_id)
            # Dumping url_list dictionary to JSON file
            with open(f'meta/{artist_f}_url_list.json', 'w') as f:
                json.dump(self.url_list, f)

        self.url_list = list(chain.from_iterable(self.url_list))
        if os.path.exists(f'meta/{artist_f}_songs.json'):
            print('Song JSON does exists. Loading file into memory...')
            with open(f'meta/{artist_f}_songs.json') as f:
                self.song_json = json.load(f)
        else:
            print('Song JSON does not exists calling getter on url list...')
            # Calls the get song lyrics method
            self.make_request(self.url_list)
            # Dumping song dictionary to JSON file
            print('Done. Saving JSON file...')
            with open(f'meta/{artist_f}_songs.json', 'w') as f:
                json.dump(self.song_dict, f)
                self.song_json = self.song_dict

        compile_lyrics.CompileLyrics(f'meta/{artist_f}_songs.json', artist)



    def get_url_list(self, id, page = 1):
        print("Getting urls of artist song for page " + str(page))
        if page == 0:
            url = 'https://api.genius.com/artists/{}/songs?sort=popularity'.format(id)
        else: 
            url = 'https://api.genius.com/artists/{}/songs?sort=popularity&page={}'.format(id, page)
        genuis_page = urllib.request.Request(url, None, ScapeLyrics.HEADER)
        genuis_html = urllib.request.urlopen(genuis_page).read().decode('utf-8')
        json_res = json.loads(genuis_html)
        song_list = json_res['response']['songs']
        page_url_list = [song['url'] for song in song_list if song['primary_artist']['id'] == id and 'annotated' not in song['url']]
        self.url_list.append(page_url_list)
        if json_res['response']['next_page'] is not None:
            self.get_url_list(id, page=json_res['response']['next_page'])

    def get_artist_id(self, artist = 'Kanye%20West'):

        artist = artist.replace(' ', '%20')
        print("Getting artist id ..")
        search_url = 'https://api.genius.com/search?q={}'.format(artist)
        print(search_url)
        search_page = urllib.request.Request(search_url, None, ScapeLyrics.HEADER)
        search_html = urllib.request.urlopen(search_page).read().decode('utf-8')
        json_res = json.loads(search_html)
        artist_id = json_res['response']['hits'][0]['result']['primary_artist']['id']
        artist_name = json_res['response']['hits'][0]['result']['primary_artist']['id']
        print("Artist found is "+ str(artist_name))
        print("Artist id is "+ str(artist_id))
        return artist_id

    def make_request(self, url_list):
        for url in url_list:
            page = urllib.request.Request(url, None, self.hdr)
            try:
                print("Getting lyric information for "+url)
                html = urllib.request.urlopen(page)
                song_soup = BeautifulSoup(html, 'lxml')
                self.scrape_data(url, song_soup)
            except urllib.error.HTTPError:
                print('Url did not work')

    def scrape_data(self, url, soup):
        for lyrics in soup.findAll("div", {"class": "lyrics"}):
            self.song_dict[url] = lyrics.text
            print("Done....") 
    
# parser = argparse.ArgumentParser(description='Scrapes Music Lyrics from artist from genuis.com.')
# parser.add_argument('--bearer_key', nargs='?', help='Add your Bearer authentication key. ')

x = ScapeLyrics('adele')