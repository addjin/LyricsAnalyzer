import config
import dummyinput

# I/O
import os

# Regex
import re

# A library that provides a Python interface to the Genius API
import lyricsgenius


genius = lyricsgenius.Genius(config.GENIUS_API_TOKEN)

artists = genius.search_artists(dummyinput.ARTIST_NAME)



print('End')