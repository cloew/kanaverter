from .kana_part import KanaPart
from .kana_sentence import KanaSentence
from .utils import is_kanji

class GroupedParser:
    """ Parser that expects the kanji and its readings to be grouped together with separator characters """
    
    def __init__(self, start_seperator='[', stop_separator=']'):
        """ Initialize the GroupParser with its start and stop separators """
        self.start_seperator = start_seperator
        self.stop_separator = stop_separator
        
    def parse(self, sentence):
        """ Parses the sentence into a KanaSentence and its KanaParts """
        parts = self.split_sentence(sentence)
        return KanaSentence(parts)
    
    def split_sentence(self, sentence):
        """ Split the sentence into the different parts """
        parts = []
        part_before_kanji, *rest = sentence.split(self.start_seperator, 1)
        if part_before_kanji != '':
            parts.append(KanaPart(part_before_kanji))
        if not rest:
          return parts
          
        part_with_kanji, *rest = rest[0].split(self.stop_separator, 1)
        if part_with_kanji != '':
            parts.append(self.split_part_with_kanji(part_with_kanji))
        if not rest:
          return parts
        
        return parts + self.split_sentence(rest[0])
        
    def split_part_with_kanji(self, part_with_kanji):
        """ Splits out the aprt with Kanji """
        indexToSplitAt = None
        for i, character in enumerate(part_with_kanji):
            if not is_kanji(character):
                indexToSplitAt = i
                break

        return KanaPart(kana=part_with_kanji[i:], kanji=part_with_kanji[:i])
