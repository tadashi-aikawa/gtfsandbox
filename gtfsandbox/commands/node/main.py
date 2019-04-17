#!/usr/bin/env python

"""
Usage:
  main.py node new <name>...
  main.py node move <lat> <lon>
  main.py node remove --type <node_type>
  main.py node (-h | --help)

Options:
  <name>                               Node name
  <lat>                                Latitude
  <lon>                                Longitude
  -t <node_type>, --type <node_type>   Node type to remove.
  -h --help                            Show this screen.
"""

from owlmixin import OwlMixin, TList, OwlEnum

from gtfsandbox.base import AbstractCmd


class CmdNew(AbstractCmd):
    class Args(OwlMixin):
        name: TList[str]

    @classmethod
    def exec(cls, args: Args):
        print(args.to_yaml())


class CmdMove(AbstractCmd):
    class Args(OwlMixin):
        lat: float
        lon: float

    @classmethod
    def exec(cls, args: Args):
        print(args.to_yaml())


class CmdRemove(AbstractCmd):
    class Args(OwlMixin):
        class Type(OwlEnum):
            STATION = "station"
            BUS_STOP = "busstop"

        type: Type

    @classmethod
    def exec(cls, args: Args):
        print(args.to_pretty_json())

