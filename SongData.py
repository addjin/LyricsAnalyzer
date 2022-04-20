class SongData:

    def __init__(self, title, artist, album, year, lyrics, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year
        self.lyrics = lyrics
        self.length = length


    def __repr__(self):
        return '{0} - {1}'.format(self.artist, self.title)
