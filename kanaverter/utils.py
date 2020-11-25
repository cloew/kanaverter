from .kana_part import KanaPart
from .kana_sentence import KanaSentence

def is_kanji(character):
    """ Return if the character is a kanji character """
    return 0x4E00 <= ord(character) <= 0x9FBF or character == '々'

def split_sentence_into_parts(sentence, readings):
    """ Splits the sentence into parts, using the readings to add the kana for any kanji based parts """
    parts = []
    current_part = ''
    parsing_kanji_part = None
    next_reading_index = 0
    
    parts = parse_simple_sentence_into_parts(sentence)
    
    for part in parts:
        if part.kanji:
            part.kana = readings[next_reading_index]
            next_reading_index += 1

    return parts
    
def parse_simple_sentence_into_parts(sentence):
    """ Parses the given simple sentence into parts """
    parts = []
    current_part = ''
    parsing_kanji_part = None
    
    for character in sentence:
        current_char_is_kanji = is_kanji(character)
        if parsing_kanji_part is None:
            parsing_kanji_part = current_char_is_kanji
        
        # If we are still parsing the same kind of section (kanji or kana)
        if current_char_is_kanji == parsing_kanji_part:
            current_part += character
        else:
            # The current part has ended and we need to build the part
            kana_part = build_kana_part(current_part, parsing_kanji_part)

            parts.append(kana_part)
            current_part = character
            parsing_kanji_part = current_char_is_kanji
            
    # Build last kana part
    kana_part = build_kana_part(current_part, parsing_kanji_part)
    parts.append(kana_part)
    
    return parts
    
    
def build_kana_part(current_part, parsing_kanji_part):
    """ Build the proper kana part based on the current processing state """
    part = None
    if parsing_kanji_part:
        part = KanaPart(kanji=current_part)
    else:
        part = KanaPart(kana=current_part)
    
    return part
