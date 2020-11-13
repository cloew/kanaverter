from .grouped_parser import GroupedParser
from .furigana_formatter import FuriganaFormatter
from .simple_formatter import SimpleFormatter

import argparse
import pyperclip

def run(args):
    """ Convert the kana sentence """
    parser = GroupedParser()
    formatter = FuriganaFormatter()
    
    sentence = parser.parse(' '.join(args))
    formatted_sentence = formatter.format(sentence)
    
    pyperclip.copy(formatted_sentence)
    print('Formatted sentence saved to Clipboard')
