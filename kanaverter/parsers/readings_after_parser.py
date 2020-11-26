from ..kana_part import KanaPart
from ..kana_sentence import KanaSentence
from ..utils import is_kanji, split_sentence_into_parts

class ReadingsAfterParser:
    """ Parser that expects the kanji readings to be included on separate lines after the simple sentence without readings """
        
    def parse(self, text_to_parse):
        """ Parses the sentence into a KanaSentence and its KanaParts """
        sentence, readings = self.get_sentence_and_readings(text_to_parse)
        parts = split_sentence_into_parts(sentence, readings)
        return KanaSentence(parts)

    def get_sentence_and_readings(self, text_to_parse):
        """ Returns the sentence text and the list of readings """
        sentence, *readings = [line for line in text_to_parse.split('\n') if line.strip()]
        return sentence, readings
