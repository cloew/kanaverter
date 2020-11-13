
class SimpleFormatter:
    """ Formatter to format a kana sentence into a simple sentence without any furigana """
    
    def format(self, sentence):
        """ Format the given KanaSentence """
        return ''.join(part.kanji or part.kana for part in sentence.parts)
