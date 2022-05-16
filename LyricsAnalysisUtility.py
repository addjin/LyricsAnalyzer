
from lazyproperty import lazy_property
import nltk
import inflection as infl
import re
from Ignorelist import is_exception_word

NOTESPATTERN = '(^\[.*\])'
SPLITPATTERN = r'\s' # TODO Fix this; it is deleting the last 's' characters of a string
TRIMNONWORDPATTERN = r'^\W|\W$'

class LyricsData:

    def __init__(self, lyrics):
        self.lyrics = lyrics

    @lazy_property
    def _tokens(self):
        _tokens = dict()
        for word in re.split(SPLITPATTERN, self._lyrics_without_notes.strip()):
            singular_word = infl.singularize(re.sub(TRIMNONWORDPATTERN, '', word).lower())
            if is_exception_word(singular_word):
                continue
            if singular_word  not in _tokens:
                _tokens[singular_word] = 0
            _tokens[singular_word] += 1
        
        return _tokens
    
    @lazy_property
    def _lyrics_without_notes(self):
        """Filters out the notes (e.g '[Chorus]', '[Verse]', etc.) from the lyrics.

            Returns:
                :obj: `str`

        """

        notes = re.findall(NOTESPATTERN, self.lyrics, re.MULTILINE)
        result =  self.lyrics
        for note in notes:
            result = result.replace(note, '')
        return re.sub(r'\n{2,}', '\n\n', result)

    @lazy_property
    def word_count(self):
        """Returns the number of words in the lyrics.
        
            Returns:
                :obj: `int`
        """
        word_count = len(self._lyrics_without_notes.strip().split(' '))
        return word_count

    @lazy_property
    def most_frequent_word(self):
        """Returns the most frequent word in the lyrics.
        
            Returns:
                :obj: `str`
        """
        count = -1
        most_frequent_word = ''
        for key in self._tokens:
            if self._tokens[key] > count:
                count = self._tokens[key]
                most_frequent_word = key
        
        return most_frequent_word

    def chorus_count(lyrics):
        pass

    def is_Match(text, match_rate=90):
        pass