#!/usr/bin/env python

import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(PROJECT_ROOT)
sys.path.append(os.getcwd())

import owcli

VERSION = '0.1.0'


def main():
    owcli.run(cli="gtfs", version=VERSION, root='gtfsandbox')


if __name__ == '__main__':
    main()
