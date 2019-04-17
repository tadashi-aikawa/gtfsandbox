"""
Usage:
  {cli} node move <lat> <lon>

Options:
  <lat>                                Latitude
  <lon>                                Longitude
"""

from owlmixin import OwlMixin


class Args(OwlMixin):
    lat: float
    lon: float


def run(args: Args):
    print(args.to_yaml())
