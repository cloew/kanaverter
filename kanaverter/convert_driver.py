from .formatters import FuriganaFormatter, SimpleFormatter
from .parsers import ParserTypes, build_parser_for_type

import argparse
import pyperclip

def run(args):
    """ Convert the kana sentence """
    argparser = argparse.ArgumentParser(description="Convert between various formats of sentences with Kanji & Kana")
    argparser.add_argument('sentence')
    argparser.add_argument('--simple', '-s', action='store_true', help="Convert output to a simple format without readings for kanji")
    argparser.add_argument('--parser', '-p', type=ParserTypes, choices=ParserTypes, help="Parser to use to read the sentence")

    parsed_args = argparser.parse_args(args)

    formatter = SimpleFormatter() if parsed_args.simple else FuriganaFormatter()
    parser = build_parser_for_type(parsed_args.parser)
    
    parse_and_format(parser, formatter, parsed_args.sentence)
    
def parse_and_format(parser, formatter, sentence_text):
    """ Parse and format the sentence text with the given parser and formatter """
    sentence = parser.parse(sentence_text)
    formatted_sentence = formatter.format(sentence)
    
    pyperclip.copy(formatted_sentence)
    print('Formatted sentence saved to Clipboard')
