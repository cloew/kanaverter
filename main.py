from kanaverter import run

import sys


def main(args):
    """ Convert the given text to the proper output format """
    run(args)

if __name__ == '__main__':
    main(sys.argv[1:])
