# -*- coding: utf-8 -*-

import sys
import argparse
import time

from projecteuler import __version__
from projecteuler import answers


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


def _seconds_to_str(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)


def exec_problem(problem):
    """ Launch problem, return result and time """

    pmodule = 'r{}'.format('%04d' % problem)

    try:
        ns = {}
        fs = 'from projecteuler.results import {} as mod'
        exec(fs.format(pmodule), globals(), ns)
        mod = ns['mod']
    except ImportError:
        return None, _seconds_to_str(0)

    start_time = time.process_time()
    # start_time = datetime.now()

    # exec_problem
    r = mod.result()

    tt = time.process_time() - start_time

    return r, _seconds_to_str(tt)


def print_result(problem, result, totaltime, expected):

    s = '{};{};{}'.format(problem, result, totaltime)

    if result:
        if expected:
            if result != expected:
                print('{};ERROR_EXPECTED:{}'.format(s, expected))
            else:
                print(s)
        else:
            print('{};ERROR_NO_ANSWER'.format(s))
    else:
        # no hay resultado
        print('{};ERROR_NO_PROBLEM_FOUND'.format(s))


def main():

    MAX_PROBLEM = 500

    parser = build_parser()
    options = parser.parse_args()

    number = options.problem

    if options.batch:
        print('PROBLEM;RESULT;TOTAL TIME')
        for n in range(number, MAX_PROBLEM):
            result, totaltime = exec_problem(n)
            # expected = solutions[n]
            expected = answers.solution(n)
            print_result(n, result, totaltime, expected)

    else:
        result, totaltime = exec_problem(number)
        expected = answers.solution(number)
        print_result(number, result, totaltime, expected)


if __name__ == '__main__':
    main()
