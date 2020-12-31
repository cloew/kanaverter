from ..kana_part import KanaPart
from ..kana_sentence import KanaSentence

class RubyParser:
    """ Parser that reads a sentence with ruby HTML tags denoting the Kanji and its readings """
        
    def parse(self, text_to_parse):
        """ Parses the sentence into a KanaSentence and its KanaParts """
        return KanaSentence([])
