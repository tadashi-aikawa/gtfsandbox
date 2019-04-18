"""Move nodes

Usage:
  {cli} node move <lat> <lon>
  {cli} (-h | --help)

Options:
  <lat>                                Latitude
  <lon>                                Longitude
  -h --help                            Show this screen.
"""

from owlmixin import OwlMixin


class Args(OwlMixin):
    lat: float
    lon: float


def run(args: Args):
    print(args.to_yaml())
