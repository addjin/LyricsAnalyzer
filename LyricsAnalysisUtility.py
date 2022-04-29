
import nltk
import re

class LyricsData:

    _tokens = None

    def __init__(self, lyrics):
        self.lyrics = lyrics
        self._most_frequent_word = None
        self._word_count = None

    def _get_tokens(self):
        if self._tokens is not None:
            return self._tokens
        else:
            self._tokens = nltk.word_tokenize(self.lyrics)
            return self._tokens

    def _remove_notes(self):
        pattern = '(^\[.*\])'
        notes = re.findall(pattern, self.lyrics, re.MULTILINE)
        result =  self.lyrics
        for note in notes:
            result = result.replace(note, '')

        return re.sub(r'\n{2,}', '\n\n', result)

    def most_frequent_word(self):
        if self._most_frequent_word is not None:
            return self._most_frequent_word
        else:
            return 'I AM THE MOST FREQUENT WORD'

    def word_count(self):
        if self._word_count is None:
            self._word_count = len(self.lyrics.strip().split(" "))
        return self._word_count

    def chorus_count(lyrics):
        pass

    def is_Match(text, match_rate=90):
        pass