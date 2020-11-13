from .grouped_parser import GroupedParser
from .formatters import FuriganaFormatter, SimpleFormatter

import argparse
import pyperclip

def run(args):
    """ Convert the kana sentence """
    argparser = argparse.ArgumentParser(description="Convert between various formats of sentences with Kanji & Kana")
    argparser.add_argument('sentence')
    argparser.add_argument('--simple', '-s', action='store_true', help="Convert output to a simple format without readings for kanji")

    parsed_args = argparser.parse_args(args)

    formatter = SimpleFormatter() if parsed_args.simple else FuriganaFormatter()
    
    parse_and_format(GroupedParser(), formatter, parsed_args.sentence)
    
def parse_and_format(parser, formatter, sentence_text):
    """ Parse and format the sentence text with the given parser and formatter """
    sentence = parser.parse(sentence_text)
    formatted_sentence = formatter.format(sentence)
    
    pyperclip.copy(formatted_sentence)
    print('Formatted sentence saved to Clipboard')
