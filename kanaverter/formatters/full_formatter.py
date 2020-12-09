
class FullFormatter:
    """ Formatter to format a kana sentence into a simple sentence without any furigana and a sentence with only the basic kana, """
    
    def format(self, sentence):
        """ Format the given KanaSentence """
        simple_sentence = self.get_simple_sentence(sentence)
        kana_sentence = self.get_kana_sentence(sentence)
        romaji_sentence = self.get_romaji_sentence(sentence)
        return '\n'.join([simple_sentence, kana_sentence, romaji_sentence])
        
    def get_simple_sentence(self, sentence):
        """ Format the given KanaSentence into a simple sentence """
        return ''.join(part.kanji or part.kana for part in sentence.parts)
        
    def get_kana_sentence(self, sentence):
        """ Format the given KanaSentence into a kana only sentence """
        return ''.join(part.kana for part in sentence.parts)
