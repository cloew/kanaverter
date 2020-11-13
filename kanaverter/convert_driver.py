import argparse
import pyperclip

def run(args):
    """ Convert the kana sentence """
    print("Running...:", args)
    
    print("Split sentence:", split_sentence(' '.join(args)))

def split_sentence(sentence):
    """ Split the sentence into the different parts """
    parts = []
    part1, *rest = sentence.split('[', 1)
    if part1 != '':
        parts.append(part1)
    if not rest:
      return parts
    part2, *rest = rest[0].split(']', 1)
    if part2 != '':
        parts.append(part2)
    if not rest:
      return parts
    
    return parts + split_sentence(rest[0])
