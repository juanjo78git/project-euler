# -*- coding: utf-8 -*-

import sys
import os
import argparse
import configparser
import importlib

from projecteuler import __version__
# from projecteuler.myproblems import p0004

def build_parser():
    """ Parser args """
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--problem', type=int,
                        dest='problem', default=None, metavar='PROBLEM',
                        help='Problem from projecteuler.net')

    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s ' + __version__)

    return parser


def main():

    parser = build_parser()
    options = parser.parse_args()

    rx = 'r{}'.format('%04d' % options.problem)
    
    ns = {}
    exec('from projecteuler.myproblems import {} as mod'.format(rx), 
         globals(), ns)
    mod = ns['mod']
    r = mod.result()
    print('Result {}: {}'.format(options.problem, r))
    

if __name__ == '__main__':
    main()
