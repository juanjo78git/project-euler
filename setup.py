#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages

import projecteuler

setup(
    name='projecteuler',
    version=projecteuler.__version__,
    packages=find_packages(),
    author='penicolas',
    author_email='png1981@gmail.com',
    description='project Euler',
    long_description="README on github : https://github.com/penicolas/project-euler",
    install_requires=[sympy],
    url='https://github.com/penicolas/project-euler',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Education',
        'Topic :: Games/Entertainment',
    ],
    entry_points={
        'console_scripts': [
            'projecteuler = projecteuler.projecteuler:main',
        ],
    },
)
