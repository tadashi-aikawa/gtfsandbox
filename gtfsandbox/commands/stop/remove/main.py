#!/usr/bin/env python

"""Remove stops

Usage:
  {cli} stop remove <name>... [-n|--with-nodes]
  {cli} (-h | --help)

Options:
  -n --with-nodes                      Action with nodes
  -h --help                            Show this screen.
"""
from owlmixin import OwlMixin, TList


class Args(OwlMixin):
    name: TList[str]
    with_nodes: bool


def run(args: Args):
    print(args.to_pretty_json())
