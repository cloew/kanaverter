from ..kana_part import KanaPart
from ..kana_sentence import KanaSentence

from bs4 import BeautifulSoup
from bs4.element import NavigableString

class RubyParser:
    """ Parser that reads a sentence with ruby HTML tags denoting the Kanji and its readings """
        
    def parse(self, text_to_parse):
        """ Parses the sentence into a KanaSentence and its KanaParts """
        parts = self.build_parts(text_to_parse)
        return KanaSentence(parts)

    def build_parts(self, text_to_parse):
        """ Parse the text as HTML and extract the readings """
        soup = BeautifulSoup(text_to_parse, 'html.parser')
        parts = []
        
        for content in soup.contents:
            if type(content) is NavigableString:
                parts.append(KanaPart(kana=content))
            elif content.name == 'ruby':
                kanji = content.contents[0]
                reading = content.contents[1].contents[0]
                parts.append(KanaPart(kanji=kanji, kana=reading))
        
        return parts
