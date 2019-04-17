"""
Usage:
  main.py node new <name>...

Options:
  <name>                               Node name
  -h --help                            Show this screen.
"""

from owlmixin import OwlMixin, TList


class Args(OwlMixin):
    name: TList[str]


def run(args: Args):
    print(args.to_yaml())
