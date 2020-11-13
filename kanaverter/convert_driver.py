from .kana_sentence import KanaSentence

import argparse
import pyperclip

def run(args):
    """ Convert the kana sentence """
    # print("Running...:", args)
    
    sentence = KanaSentence.parse(' '.join(args))
    pyperclip.copy(str(sentence))
