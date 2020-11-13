from .grouped_parser import GroupedParser

import argparse
import pyperclip

def run(args):
    """ Convert the kana sentence """
    sentence = GroupedParser().parse(' '.join(args))
    pyperclip.copy(str(sentence))
    print('Sentence saved to Clipboard')
