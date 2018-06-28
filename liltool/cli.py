"""
Usage:
    lil (-h | --help)
    lil [-v | --verbose] <command> [<args>...]

Global options:
    -h, --help          Show a brief usage summary.
    -v, --verbose       Increase verbosity of output.

Commands:
    learners            Manipulate list of registered learners.

"""
import logging
import sys

import docopt

from . import learners


LOG = logging.getLogger('lil')


COMMAND_MAIN_FUNCTIONS = {
    'learners': learners.main,
}


def main():
    opts = docopt.docopt(__doc__, options_first=True)

    logging.basicConfig(
        level=logging.INFO if opts['--verbose'] else logging.WARN
    )

    command_main = COMMAND_MAIN_FUNCTIONS.get(opts['<command>'])
    if command_main is None:
        LOG.error('%s: unknown command', command_main)
        sys.exit(1)

    command_main([opts['<command>']] + opts['<args>'])
