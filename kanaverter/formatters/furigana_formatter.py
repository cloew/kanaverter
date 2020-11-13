
class FuriganaFormatter:
    """ Formatter to format a kana sentence into a sentence with html for furigana readings of the kanji """
    
    def format(self, sentence):
        """ Format the given KanaSentence """
        return ''.join(self.build_string_for_part(part) for part in sentence.parts)
    
    def build_string_for_part(self, part):
        """ Build the string for the given part """
        if part.kanji:
            return self.build_kanji_part(part)
        else:
            return self.build_simple_part(part)
            
    def build_kanji_part(self, part):
        """ Return the ruby html element and its readings for the given part """
        return "<ruby>{part.kanji}<rt>{part.kana}</rt></ruby>".format(part=part)
            
    def build_simple_part(self, part):
        """ Return the simple kana part without any extra hmtl """
        return part.kana
