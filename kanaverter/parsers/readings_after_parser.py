from ..kana_part import KanaPart
from ..kana_sentence import KanaSentence
from ..utils import is_kanji

class ReadingsAfterParser:
    """ Parser that expects the kanji readings to be included on separate lines after the simple sentence without readings """
        
    def parse(self, text_to_parse):
        """ Parses the sentence into a KanaSentence and its KanaParts """
        sentence, readings = self.get_sentence_and_readings(text_to_parse)
        parts = self.split_sentence_into_parts(sentence, readings)
        return KanaSentence(parts)

    def get_sentence_and_readings(self, text_to_parse):
        """ Returns the sentence text and the list of readings """
        sentence, *readings = [line for line in text_to_parse.split('\n') if line.strip()]
        return sentence, readings

    def split_sentence_into_parts(self, sentence, readings):
        """ Splits the sentence into parts, using the readings to add the kana for any kanji based parts """
        parts = []
        current_part = ''
        parsing_kanji_part = None
        next_reading_index = 0
        
        for character in sentence:
            current_char_is_kanji = is_kanji(character)
            if parsing_kanji_part is None:
                parsing_kanji_part = current_char_is_kanji
            
            # If we are still parsing the same kind of section (kanji or kana)
            if current_char_is_kanji == parsing_kanji_part:
                current_part += character
            else:
                # The current part has ended and we need to build the part
                kana_part = self.build_kana_part(current_part, parsing_kanji_part, readings, next_reading_index)
                if kana_part.kanji:
                    next_reading_index += 1
                # if parsing_kanji_part:
                    # parts.append(KanaPart(kanji=current_part, kana=readings[next_reading_index]))
                # else:
                    # parts.append(KanaPart(kana=current_part))
                parts.append(kana_part)
                current_part = character
                parsing_kanji_part = current_char_is_kanji
                
        # Build last kana part
        kana_part = self.build_kana_part(current_part, parsing_kanji_part, readings, next_reading_index)
        parts.append(kana_part)

        return parts
        
    def build_kana_part(self, current_part, parsing_kanji_part, readings, next_reading_index):
        """ Build the proper kana part based on the current processing state """
        part = None
        if parsing_kanji_part:
            part = KanaPart(kanji=current_part, kana=readings[next_reading_index])
        else:
            part = KanaPart(kana=current_part)
        
        return part
