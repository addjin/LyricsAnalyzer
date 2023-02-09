
from enum import unique
from lazyproperty import lazy_property
import nltk
import inflection as infl
import re
from StringUtility import *
from Ignorelist import is_exception_word


class LyricsData:

    def __init__(self, songTitle, rawLyrics, removesTitle=True):
        self.title = songTitle
        self.rawLyrics = rawLyrics
        self.lyrics = rawLyrics
        self._edit_lyrics()

        if (removesTitle):
            self._remove_title()

    @lazy_property
    def _tokens(self):
        _tokens = dict()
        for word in re.split(SPLITPATTERN, self._lyrics_without_notes.strip()):
            singular_word = infl.singularize(
                re.sub(TRIMNONWORDPATTERN, '', word).lower())
            if is_exception_word(singular_word):
                # TODO make sure to input the right parameters into is_exception_word() (ignorecase, ignorepronouns, etc.)
                continue
            if singular_word not in _tokens:
                _tokens[singular_word] = 0
            _tokens[singular_word] += 1

        return _tokens

    @lazy_property
    def _lyrics_without_notes(self):
        """
        Filters out the notes (e.g '[Chorus]', '[Verse]', etc.) from the lyrics.

            Returns:
                `str`
        """

        notes = re.findall(NOTESPATTERN, self.lyrics)
        result = self.lyrics
        for note in notes:
            result = result.replace(note, '')
        return re.sub(r'\n{2,}', '\n\n', result)

    @lazy_property
    def word_count(self):
        """
        Returns the number of words in the lyrics.

            Returns:
                `int`
        """

        return len(self._lyrics_without_notes.strip().split(' '))

    @lazy_property
    def unique_word_count(self):
        """
        Returns the number of unique words in the lyrics.

            Returns:
                `int`
        """

        return len(self._tokens)

    @lazy_property
    def most_frequent_word(self):
        """
        Returns the most frequent word in the lyrics.

            Returns:
                `str`
        """
        count = -1
        most_frequent_word = ''
        for key in self._tokens:
            if self._tokens[key] > count:
                count = self._tokens[key]
                most_frequent_word = key

        return most_frequent_word

    @lazy_property
    def chorus_count(self):
        """
            Returns the number of choruses in the lyrics.

            Returns:
                `None`
        """
        return len(re.findall(r'\[chorus\]', self.lyrics, re.IGNORECASE))

    def _edit_lyrics(self):
        """
        Edits the lyrics field of the object. Called during the initialization of the object, right after the assignment of lyrics.

            Returns:
                `None`
        """

        self._remove_quotations()

        newlines = re.findall(NEWLINEPATTERN, self.lyrics, re.MULTILINE)

        for newline in newlines:
            self.lyrics = self.lyrics.replace(newline, '\n')

        self._remove_embed_pattern()

    def _remove_quotations(self):
        """
        Removes the quotation marks at the beginning and the end of the lyrics.

        Returns:
            `None`
        """
        self.lyrics = self.lyrics.strip('"')

    def _remove_embed_pattern(self):
        """
         As of 2023/02/08, For some reason, there is a pattern in the form of "[0-9]Embed" at the end of the lyrics obtained from Genius. 
         This method removes all the strings obeying this pattern.

         Returns:
            `None`
        """
        embedPattern = r'[0-9]embed'
        self.lyrics = re.sub(pattern=embedPattern, repl='', string=self.lyrics)

    def _remove_title(self):
        """
        Removes the title from the lyrics.

        Returns:
            `None`
        """
        firstLine, restOfLyrics = self.lyrics.split("\n", 1)
        titleStrings = re.findall(self.title, firstLine, re.IGNORECASE)
        lyricsStrings = re.findall("lyrics", firstLine, re.IGNORECASE)

        for title in titleStrings:
            firstLine = firstLine.replace(title, '')

        for lyricsString in lyricsStrings:
            firstLine = firstLine.replace(lyricsString, '')

        self.lyrics = (firstLine + '\n' + restOfLyrics).strip()


    def clear_chorus():
        #TODO this method will clear all the choruses except for the first one.
        # One way to define a chorus is to get everything from [Chorus] to next empty line (or the next [Note]).
        # TODO If for example the last chorus is a bit different, should it keep the whole chorus or filter out the common parts?
        pass

    def is_Match(text, match_rate=90):
        pass
