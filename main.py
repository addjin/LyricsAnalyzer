import config
import dummyinput
import GeniusAPICustomUtility as GeniusUtil

# I/O
import os

# Regex
import re

artist_Name = dummyinput.ARTIST_NAME

artistNameArtistMap = GeniusUtil.get_artistName_artist_map(artist_Name)

if len(artistNameArtistMap) == 0:
    print('No results for artist \'{0}\'.'.format(artist_Name))
    exit()
else:
    print('Candidates:')

    enumeratedArtistMap = {}

    for i, (key, val) in enumerate(artistNameArtistMap.items()):
        enumeratedArtistMap[str(i)] = val
        print('\t{0}: {1}'.format(i, key))

inp = input('Input the number of the artist (or \'x\' to quit):')
while inp not in enumeratedArtistMap.keys() and inp != 'x':
    inp = input('Invalid input; please try again')

if inp == 'x':
    exit()
else:
    selected_artist = enumeratedArtistMap[inp]

print('End')