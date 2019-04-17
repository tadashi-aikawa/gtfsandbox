#!/usr/bin/env python

"""
Usage:
  main.py stop new <name>... [-n|--with-nodes]
  main.py stop remove <name>... [-n|--with-nodes]
  main.py stop (-h | --help)

Options:
  -n --with-nodes                      Action with nodes
  -h --help                            Show this screen.
"""
from owlmixin import OwlMixin, TList

from gtfsandbox.base import AbstractCmd


class CmdNew(AbstractCmd):
    class Args(OwlMixin):
        name: TList[str]
        with_nodes: bool

    @classmethod
    def exec(cls, args: Args):
        print(args.to_yaml())


class CmdRemove(AbstractCmd):
    class Args(OwlMixin):
        name: TList[str]
        with_nodes: bool

    @classmethod
    def exec(cls, args: Args):
        print(args.to_pretty_json())

