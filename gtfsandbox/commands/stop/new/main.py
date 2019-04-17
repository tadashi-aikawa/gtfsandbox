#!/usr/bin/env python

"""
Usage:
  main.py stop new <name>... [-n|--with-nodes]

Options:
  -n --with-nodes                      Action with nodes
  -h --help                            Show this screen.
"""
from owlmixin import OwlMixin, TList


class Args(OwlMixin):
    name: TList[str]
    with_nodes: bool


def run(args: Args):
    print(args.to_yaml())
