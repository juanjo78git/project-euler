# -*- coding: utf-8 -*-

import sys
import os
import argparse
import configparser
import importlib

from projecteuler import __version__
from datetime import datetime
# from projecteuler.myproblems import p0004

def build_parser():
    """ Parser args """
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--problem', type=int, required=True,
                        dest='problem', metavar='PROBLEM',
                        help='Problem from projecteuler.net')
    
    parser.add_argument('-b', '--batch-mode', action='store_true',
                        dest='batch', default=False,
                        help='Batch mode')
    
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s ' + __version__)

    return parser


def exec_problem(problem):
    """ Launch problem, return result and time """
    
    pmodule = 'r{}'.format('%04d' % problem)

    ns = {}
    fs = 'from projecteuler.results import {} as mod'
    exec(fs.format(pmodule), globals(), ns)
    mod = ns['mod']

    start_time = datetime.now()

    # exec_problem
    r = mod.result()

    tt = datetime.now() - start_time

    return r, tt





def main():

    solutions = {1: 233168,
                      2: 4613732,
                      3: 6857,
                      4: 906609,
                      5: 232792560,
                      6: 25164150,
                      7: 104743,
                      8: 23514624000,
                      9: 31875000,
                      10: 142913828922,
                      11: 70600674,
                      12: 76576500,
                      13: 5537376230,
                      14: 837799,
                      15: 137846528820,
                      16: 1366,
                      17: 21124,
                      18: 1074,
                      19: 171,
                      20: 648,
                      21: 31626,
                      22: 871198282,
                      23: 4179871,
                      24: 2783915460,
                      25: 4782,
                      26: 983,
                      27: -59231,
                      28: 669171001,
                      29: 9183,
                      30: 443839,
                      31: 73682,
                      32: 45228,
                      33: 100,
                      34: 40730,
                      35: 55,
                      36: 872187,
                      37: 748317,
                      38: 932718654,
                      39: 840,
                      40: 210,
                      41: 7652413,
                      42: 162,
                      43: 16695334890,
                      44: 5482660,
                      45: 1533776805,
                      46: 5777,
                      47: 134043,
                      48: 9110846700,
                      49: 296962999629,
                      50: 997651,
                      51: 121313,
                      52: 142857,
                      53: 4075,
                      54: 376,
                      55: 249,
                      56: 972,
                      57: 153,
                      58: 26241,
                      59: 107359,
                      60: 26033,
                      61: 28684,
                      62: 127035954683,
                      63: 49,
                      64: 1322,
                      65: 272,
                      66: 661,
                      67: 7273,
                      68: 6531031914842725,
                      69: 510510,
                      70: 8319823,
                      71: 428570,
                      72: 303963552391,
                      73: 7295372,
                      74: 402,
                      75: 161667,
                      76: 190569291,
                      77: 71,
                      78: 55374,
                      79: 73162890,
                      80: 40886,
                      81: 427337,
                      82: 260324,
                      83: 425185,
                      84: 101524,
                      85: 2772,
                      86: 1818,
                      87: 1097343,
                      88: 7587457,
                      89: 743,
                      90: 1217,
                      91: 14234,
                      92: 8581146,
                      93: 1258,
                      94: 518408346,
                      95: 14316,
                      96: 24702,
                      97: 8739992577,
                      98: 18769,
                      99: 709,
                      100: 756872327473}

    MAX_PROBLEM = 50

    parser = build_parser()
    options = parser.parse_args()

    number = options.problem

    if options.batch:
        print('PROBLEM;RESULT;TOTAL TIME')
        for n in range(number, MAX_PROBLEM):
            result, totaltime = exec_problem(n)
            expected = solutions[n]
            if result != expected:
                print('Problem: {}, Result: {}, Expected: {}'.format(n,
                                                                     result,
                                                                     expected))
                # raise NameError('Invalid result')
                sys.exit(2)
            print('{};{};{}'.format(n, result, totaltime))
    else:
        result, totaltime = exec_problem(number)
        expected = solutions[number]
        if result != expected:
            print('Problem: {}, Result: {}, Expected: {}'.format(number,
                                                                 result,
                                                                 expected))
            # raise NameError('Invalid result')
            sys.exit(2)
        print('Problem: {}, Result: {}, TotalTime: {}'.format(number,
                                                              result,
                                                              totaltime))


if __name__ == '__main__':
    main()
