#!/usr/bin/env python

"""
Usage:
  main.py info [-v|-vv|-vvv]

Options:
  -v                                   Verbose (`-v` or `-vv` or `-vvv`)
  -h --help                            Show this screen.
"""
from owlmixin import OwlMixin

from gtfsandbox.base import AbstractCmd


class Cmd(AbstractCmd):
    class Args(OwlMixin):
        v: int

    @classmethod
    def exec(cls, args: Args):
        print(args.to_yaml())
