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
    """Gets all the albums of the specified artist.
    
        Args:
            artist (:obj: `lyricsgenius.types.Artist`): Artist.
            filtersSpecialEditions (:obj: `bool`, optional): Filter special edition albums.

        Returns:
            :obj: `list`
    
    """

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


def get_lyrics_from_album(album):
    """Gets all the lyrics from the an Album object.
    
    Args:
        album (:obj: `lyricsgenius.types.Album`): The album from which the tracks and their lyrics to be obtained.

    Returns:
        :obj: `dict`
    
    """

    track_lyrics_map = {}

    for track in album.tracks:
        track_lyrics_map[track.song.title] = track.song.lyrics
    
    return track_lyrics_map

