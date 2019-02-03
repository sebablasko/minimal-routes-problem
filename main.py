#!/usr/bin/env python
import sys
import os.path
from argparse import ArgumentParser
from dijsktra import dijsktra
from dial import dial
from utils import printResult, saveResult


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("El archivo %s no existe" % arg)
    else:
        return open(arg, 'r')


if __name__ == '__main__':
    parser = ArgumentParser(description="""Runs Dijsktra algorithm.
                        Stores the output in a file.""")
    parser.add_argument("nodosfile",
                        help="file with nodos information",
                        metavar="nodosfile",
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument("arcosfile",
                        help="File with arcos information",
                        metavar="arcosfile",
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument("originnode",
                        help="Number of the origin node",
                        metavar="originnode",
                        type=int)
    parser.add_argument("--dial",
                        help="Use the Dial's Dijsktra implementation",
                        action="store_true")
    parser.add_argument("--so",
                        help="""print results in standard output instead
                        create a file""",
                        action="store_true")
    args = parser.parse_args()

    if args.dial:
        print('Running Dial')
        algorithm = dial
    else:
        print('Running distra')
        algorithm = dijsktra
    # Start
    result = algorithm(args.nodosfile, args.arcosfile, args.originnode)
    # Output
    if args.so:
        printResult(args.originnode, result)
    else:
        saveResult(args.originnode, result)
    # Close files
    args.nodosfile.close()
    args.arcosfile.close()
