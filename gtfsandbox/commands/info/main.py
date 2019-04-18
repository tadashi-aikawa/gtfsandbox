"""Show information

Usage:
  {cli} info [-v|-vv|-vvv]
  {cli} (-h | --help)

Options:
  -v                                   Verbose (`-v` or `-vv` or `-vvv`)
  -h --help                            Show this screen.
"""
from owlmixin import OwlMixin


class Args(OwlMixin):
    v: int


def run(args: Args):
    print(args.to_yaml())
