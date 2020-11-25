
class KanaPart:
    """ Represents part of a sentence with its kana or kanji and its reading in kana """
    
    def __init__(self, kana='', kanji=''):
        """ Initialize the part with its kana and optionally the kanji as well """
        self.kana = kana
        self.kanji = kanji
