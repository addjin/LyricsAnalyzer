import config

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

def get_all_albums(artist, filtersSpecialEditions=True):
    albumDataList = geniusAPI.artist_albums(artist_id=artist['id'])['albums']

    albumList = []

    for albumData in albumDataList:

        if filtersSpecialEditions and __is_specialedition(albumDataList, albumData['name']):
            continue

        albumList.append(geniusAPI.search_album(album_id=albumData['id'], get_full_info=False))


    return albumList


def __is_specialedition(albumDataList, albumName):
    # TODO implement later with keywords such as "Deluxe", "Special Edition", etc.
    # TODO you can also check other parameters (if the release dates are the same, track title comparison, etc.)
    return False
