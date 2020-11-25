from ..kana_part import KanaPart
from ..kana_sentence import KanaSentence
from ..utils import is_kanji, split_sentence_into_parts

class JishoParser:
    """ Parser that expects the kanji readings to be on separate lines within the sentence as happens when copying from Jisho.org """
        
    def parse(self, text_to_parse):
        """ Parses the sentence into a KanaSentence and its KanaParts """
        sentence, readings = self.get_sentence_and_readings(text_to_parse)
        parts = split_sentence_into_parts(sentence, readings)
        return KanaSentence(parts)

    def get_sentence_and_readings(self, text_to_parse):
        """ Returns the sentence text and the list of readings """
        normal_lines = []
        readings = []
        
        
        lines = [line for line in text_to_parse.split('\n') if line.strip()]
        
        if len(lines) == 1:
            return lines[0], []
        
        for i, line in enumerate(lines):
            if i == 0:
                continue
                
            if is_kanji(line[0]):
                print('Previous line has reading:', i)
                normal_lines.append(line)
                readings.append(lines[i-1])
            elif i == 1:
                normal_lines.append(lines[0])
            
        return "".join(normal_lines), readings
