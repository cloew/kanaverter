from ..kana_sentence import KanaSentence
from ..utils import parse_simple_sentence_into_parts

class MyFormatParser:
    """ Parser that expects the simple sentence and the sentence in only kana AKA the format I've been using in Anki """
        
    def parse(self, text_to_parse):
        """ Parses the sentence into a KanaSentence and its KanaParts """
        simple_sentence, kana_sentence = self.get_sentences(text_to_parse)
        parts = self.build_parts(simple_sentence, kana_sentence)
        return KanaSentence(parts)

    def get_sentences(self, text_to_parse):
        """ Return the simple sentence and the kana sentence """
        simple_sentence, *rest = text_to_parse.split('(', 1)
        kana_sentence, *rest = rest[0].split(')', 1)
        return simple_sentence.strip(), kana_sentence.strip().replace(' ', '')

    def build_parts(self, simple_sentence, kana_sentence):
        """ Build the KanaParts for each line with its first reading """
        parts = parse_simple_sentence_into_parts(simple_sentence)
        
        remaining_sentence = kana_sentence
        
        for i, part in enumerate(parts):
            if part.kanji:
                if i+1 == len(parts):
                    part.kana = remaining_sentence
                else:
                    start_of_next_part = remaining_sentence.find(parts[i+1].kana)
                    part.kana = remaining_sentence[:start_of_next_part]
                    remaining_sentence = remaining_sentence[start_of_next_part:]
            else:
                remaining_sentence = remaining_sentence.replace(part.kana, '', 1)
        
        return parts
