#!/usr/bin/env python

import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(PROJECT_ROOT)
sys.path.append(os.getcwd())

import docowl

VERSION = '0.1.0'
COMMANDS = '''
node       Action for nodes
stop       Action for stops
info       Show information
'''


def main():
    docowl.run(cli="gtfs", commands=COMMANDS, version=VERSION, root='gtfsandbox')


if __name__ == '__main__':
    main()
