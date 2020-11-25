from ..kana_part import KanaPart
from ..kana_sentence import KanaSentence
from ..utils import is_kanji, split_sentence_into_parts, parse_simple_sentence_into_parts

class JishoParser:
    """ Parser that expects the kanji readings to be on separate lines within the sentence as happens when copying from Jisho.org """
        
    def parse(self, text_to_parse):
        """ Parses the sentence into a KanaSentence and its KanaParts """
        lines_and_first_readings = self.get_lines_with_first_reading(text_to_parse)
        parts = self.build_parts(lines_and_first_readings)
        return KanaSentence(parts)
    
    def build_parts(self, lines_and_first_readings):
        """ Build the KanaParts for each line with its first reading """
        parts = []
        
        for line, first_reading in lines_and_first_readings:
            parts_for_line = parse_simple_sentence_into_parts(line)
            if parts_for_line[0].kanji and first_reading:
                parts_for_line[0].kana = first_reading
            parts.extend(parts_for_line)
        
        return parts

    def get_lines_with_first_reading(self, text_to_parse):
        """ Returns the list of lines and their first reading, if they have one """
        lines_and_first_readings = []
        lines = [line for line in text_to_parse.split('\n') if line.strip()]
        
        for i, line in enumerate(lines):
            if i == 0:
                continue
                
            if is_kanji(line[0]):
                lines_and_first_readings.append((line, lines[i-1]))
            elif i == 1:
                lines_and_first_readings.append((lines[0], None))
            
        return lines_and_first_readings
