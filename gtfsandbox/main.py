#!/usr/bin/env python

"""GTFS commands.

Usage:
  main.py <command> [<subcommand>] [<args>...]
  main.py [<command>] (-h | --help)
  main.py --version

Commands:
  node       Action for nodes
  stop       Action for stops
  info       Show information
"""
import os
import sys
from docopt import docopt
from importlib import import_module

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(PROJECT_ROOT)
sys.path.append(os.getcwd())

VERSION = '0.1.0'


def command_not_found_format(command: str) -> str:
    return f"""
Command `{command}` is not found.
Show available commands.
-------------------------------------
"""


def subcommand_not_found_format(subcommand: str, command: str) -> str:
    return f"""
Subcommand `{subcommand}` is not found in `{command}` command.
Show available subcommands.
---------------------------------------
"""


def head2upper(value: str) -> str:
    return value[0].upper() + value[1:]


def main():
    # Remove <args> to avoid parse errors.
    main_args = docopt(__doc__, argv=sys.argv[1:3], version=VERSION, options_first=True)

    command: str = main_args.pop('<command>')
    try:
        cmd_module = import_module(f'gtfsandbox.commands.{command}.main')
    except ModuleNotFoundError:
        print(command_not_found_format(command))
        print(__doc__)
        sys.exit(1)

    subcommand: str = main_args.pop('<subcommand>')
    # Show global docs and abort
    if subcommand in ["-h", "--help", None]:
        print(cmd_module.__doc__)
        sys.exit(0)

    try:
        # Run without subcommand if there are no subcommands
        getattr(cmd_module, 'Cmd').run(cmd_module.__doc__)
    except AttributeError:
        # Subcommand exists
        try:
            getattr(cmd_module, f'Cmd{head2upper(subcommand)}').run(cmd_module.__doc__)
        except AttributeError as e:
            print(e)
            print(subcommand_not_found_format(subcommand, command))
            print(cmd_module.__doc__)
            sys.exit(1)


if __name__ == '__main__':
    main()
