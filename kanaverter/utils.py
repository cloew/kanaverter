
def is_kanji(character):
    """ Return if the character is a kanji character """
    return 0x4E00 <= ord(character) <= 0x9FBF