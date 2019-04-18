"""Create nodes

Usage:
  {cli} node new <name>...
  {cli} (-h | --help)

Options:
  <name>                               Node name
  -h --help                            Show this screen.
"""

from owlmixin import OwlMixin, TList


class Args(OwlMixin):
    name: TList[str]


def run(args: Args):
    print(args.to_yaml())
