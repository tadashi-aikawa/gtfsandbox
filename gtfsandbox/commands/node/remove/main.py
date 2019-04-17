"""
Usage:
  {cli} node remove --type <node_type>

Options:
  -t <node_type>, --type <node_type>   Node type to remove.
  -h --help                            Show this screen.
"""

from owlmixin import OwlMixin, OwlEnum


class Type(OwlEnum):
    STATION = "station"
    BUS_STOP = "bus_stop"


class Args(OwlMixin):
    type: Type


def run(args: Args):
    print(args.to_pretty_json())
