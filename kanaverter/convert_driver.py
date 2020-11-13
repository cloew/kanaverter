from .kana_sentence import KanaSentence

import argparse
import pyperclip

def run(args):
    """ Convert the kana sentence """
    sentence = KanaSentence.parse(' '.join(args))
    pyperclip.copy(str(sentence))
    print('Sentence saved to Clipboard')
