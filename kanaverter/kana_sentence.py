
class KanaSentence:
    """ Represents a sentence with kana and kanji """

    def __init__(self, parts):
        """ Initialize the Sentence with its parts """
        self.parts = parts
    
    def __str__(self):
        """ Convert the sentence to a string """
        return ''.join(str(part) for part in self.parts)
