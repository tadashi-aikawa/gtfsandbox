#!/usr/bin/env python

"""GTFS commands.

Usage:
  main.py node new <name>...
  main.py node move <lat> <lon>
  main.py node remove --type <node_type>
  main.py stop (new|remove) <name>... [-n|--with-nodes]
  main.py info [-v|-vv|-vvv]
  main.py (-h | --help)
  main.py --version

Options:
  -h --help                            Show this screen.
  --version                            Show version.
  <lat>                                Latitude
  <lon>                                Longitude
  -n, --with-nodes                     Action with nodes
  -t <node_type>, --type <node_type>   Node type to remove.
  -v                                   Verbose (`-v` or `-vv` or `-vvv`)
"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    print(arguments)
