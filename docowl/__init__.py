import sys
from importlib import import_module

from docopt import docopt

_DOC_TMPL_ = """
Usage:
  {cli} <command> [<subcommand>] [<args>...]
  {cli} [<command>] (-h | --help)
  {cli} --version

Commands:
{commands}
"""


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


def run(cli: str, commands: str, version: str, root: str):
    """
    :param cli: CLI file name
    :param commands: command names
    :param version: version
    :param root: root package path

    Example:
        ----
        VERSION = '0.1.0'
        COMMANDS = '''
        node       Action for nodes
        stop       Action for stops
        info       Show information
        '''

        docowl.run(cli="gtfs", commands=COMMANDS, version=VERSION, root='gtfsandbox')
        ----
    """
    # Remove <args> to avoid parse errors.
    doc = _DOC_TMPL_.format(cli=cli, commands='\n'.join([f'  {x}' for x in commands.strip().split('\n')]))
    main_args = docopt(doc, argv=sys.argv[1:3], version=version, options_first=True)

    command: str = main_args.pop('<command>')
    try:
        cmd_module = import_module(f'{root}.commands.{command}.main')
    except ModuleNotFoundError:
        print(command_not_found_format(command))
        print(doc)
        sys.exit(1)

    subcommand: str = main_args.pop('<subcommand>')
    # Show global docs and abort
    if subcommand in ["-h", "--help", None]:
        print(cmd_module.__doc__)
        sys.exit(0)

    try:
        # Run without subcommand if there are no subcommands
        cmd_module.run(
            cmd_module.Args.from_dict(docopt(cmd_module.__doc__), restrict=False, force_cast=True)
        )
    except AttributeError:
        # Subcommand exists
        try:
            sub_cmd_module = import_module(f'gtfsandbox.commands.{command}.{subcommand}.main')
            sub_cmd_module.run(
                sub_cmd_module.Args.from_dict(docopt(sub_cmd_module.__doc__), restrict=False, force_cast=True)
            )
        except AttributeError as e:
            print(e)
            print(subcommand_not_found_format(subcommand, command))
            print(cmd_module.__doc__)
            sys.exit(1)
        except ModuleNotFoundError as e:
            print(e)
            print(subcommand_not_found_format(subcommand, command))
            print(cmd_module.__doc__)
            sys.exit(1)