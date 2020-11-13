from .grouped_parser import GroupedParser
from .simple_formatter import SimpleFormatter

import argparse
import pyperclip

def run(args):
    """ Convert the kana sentence """
    parser = GroupedParser()
    formatter = SimpleFormatter()
    
    sentence = parser.parse(' '.join(args))
    formatted_sentence = formatter.format(sentence)
    
    pyperclip.copy(formatted_sentence)
    print('Formatted sentence saved to Clipboard')
