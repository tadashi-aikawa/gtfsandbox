#!/usr/bin/env python

"""
Usage:
  main.py info [-v|-vv|-vvv]

Options:
  -v                                   Verbose (`-v` or `-vv` or `-vvv`)
  -h --help                            Show this screen.
"""
from owlmixin import OwlMixin


class Args(OwlMixin):
    v: int


def run(args: Args):
    print(args.to_yaml())
