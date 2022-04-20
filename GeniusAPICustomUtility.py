import config
import re

# A library that provides a Python interface to the Genius API
import lyricsgenius

geniusAPI = lyricsgenius.Genius(config.GENIUS_API_TOKEN)

def get_artist_names(name):
    hitsList = geniusAPI.search_artists(name, per_page=3)['sections'][0]['hits']

    return hitsList

