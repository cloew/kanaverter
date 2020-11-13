from .kana_part import KanaPart
from .utils import is_kanji

def split_sentence(sentence):
    """ Split the sentence into the different parts """
    parts = []
    part1, *rest = sentence.split('[', 1)
    if part1 != '':
        parts.append(KanaPart(part1))
    if not rest:
      return parts
    partWithKanji, *rest = rest[0].split(']', 1)
    if partWithKanji != '':
        parts.append(split_part_with_kanji(partWithKanji))
    if not rest:
      return parts
    
    return parts + split_sentence(rest[0])
    
def split_part_with_kanji(partWithKanji):
    """ Splits out the aprt with Kanji """
    indexToSplitAt = None
    for i, character in enumerate(partWithKanji):
        if not is_kanji(character):
            indexToSplitAt = i
            break
    return KanaPart(kana=partWithKanji[i:], kanji=partWithKanji[:i])
    
class KanaSentence:
    """ Represents a sentence with kana and kanji """

    @classmethod
    def parse(cls, sentence):
       """ Parses the sentence into an instance of the given class """
       parts = split_sentence(sentence)
       return cls(parts)

    def __init__(self, parts):
        """ Initialize the Sentence with its parts """
        self.parts = parts
    
    def __str__(self):
        """ Convert the sentence to a string """
        return ''.join(str(part) for part in self.parts)
