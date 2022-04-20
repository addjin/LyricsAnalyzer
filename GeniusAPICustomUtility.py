import config
import re

# A library that provides a Python interface to the Genius API
import lyricsgenius

geniusAPI = lyricsgenius.Genius(config.GENIUS_API_TOKEN)

def get_artistName_artist_map(name):
    hitsList = geniusAPI.search_artists(name)['sections'][0]['hits']

    hitsDict = {}

    for hit in hitsList:
        res = hit['result']
        hitsDict[res['name']] = res

    return hitsDict

def get_all_albums(artist):
    albumsList = geniusAPI.artist_albums(artist_id=artist['id'])['albums']

    # for album in albumsList:


    return albumsList