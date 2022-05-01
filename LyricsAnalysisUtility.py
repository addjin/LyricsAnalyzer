
from lazyproperty import lazy_property
import nltk
import inflection as infl
import re

NOTESPATTERN = '(^\[.*\])'
SPLITPATTERN = '\s' # TODO Fix this; it is deleting the last 's' characters of a string

class LyricsData:

    def __init__(self, lyrics):
        self.lyrics = lyrics

    @lazy_property
    def _tokens(self):
        _tokens = dict()
        for word in re.split(SPLITPATTERN, self._lyrics_without_notes.strip()):
            # TODO Fix this
            singular_word = infl.singularize(re.sub('\W', '', word) .lower())
            if singular_word  not in _tokens:
                _tokens[singular_word] = 0
            _tokens[singular_word] += 1
        
        return _tokens
    
    @lazy_property
    def _lyrics_without_notes(self):
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

    def get_most_frequent_word(self):
        """Returns the most frequent word in the lyrics.
        
            Returns:
                :obj: `str`
        
        """
        if self._most_frequent_word is None:
            count = -1
            for key in self.tokenz:
                if self.tokenz[key] > count:
                    count = self.tokenz[key]
                    self._most_frequent_word = self._tokens[key]
        
        return self._most_frequent_word

    def chorus_count(lyrics):
        pass

    def is_Match(text, match_rate=90):
        pass