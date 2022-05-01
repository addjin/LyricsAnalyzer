from LyricsAnalysisUtility import LyricsData
import dummyinput
import GeniusAPICustomUtility as GeniusUtil

artist_Name = dummyinput.ARTIST_NAME

# artistNameArtistMap = GeniusUtil.get_artistName_artist_map(artist_Name)

# if len(artistNameArtistMap) == 0:
#     print('No results for artist \'{0}\'.'.format(artist_Name))
#     exit()
# else:
#     print('Candidates:')

#     enumeratedArtistMap = {}

#     for i, (key, val) in enumerate(artistNameArtistMap.items()):
#         enumeratedArtistMap[str(i)] = val
#         print('\t{0}: {1}'.format(i, key))

# inp = input('Input the number of the artist (or \'x\' to quit):')
# while inp not in enumeratedArtistMap.keys() and inp != 'x':
#     inp = input('Invalid input; please try again')

# if inp == 'x':
#     exit()
# else:
#     selected_artist = enumeratedArtistMap[inp]


# all_albums_list = GeniusUtil.get_all_albums(selected_artist)
# track_lyrics_map = GeniusUtil.get_lyrics_from_album(all_albums_list[0])

my_lyrics_data = None

with open('squarehammer.txt', 'r') as samplelyrics:
    my_lyrics_data = LyricsData(samplelyrics.read())

print(my_lyrics_data._lyrics_without_notes)
print(my_lyrics_data.word_count)
print(my_lyrics_data._tokens)

print('End')


