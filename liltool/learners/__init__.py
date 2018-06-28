"""
Usage:
    lil learners (-h | --help)
    lil learners <command> [<args>...]

Commands:
    help                Show a brief usage summary.
    update              Update Learner list from Lookup group.

"""
import logging
import sys

import docopt

from . import update


LOG = logging.getLogger('lil learners')


def show_help(argv):
    print(__doc__)


COMMAND_MAIN_FUNCTIONS = {
    'update': update.main,
    '-h': show_help,
    '--help': show_help,
}


def main(argv):
    opts = docopt.docopt(__doc__, argv=argv, options_first=True)

    command_main = COMMAND_MAIN_FUNCTIONS.get(opts['<command>'])
    if command_main is None:
        LOG.error('%s: unknown command', command_main)
        sys.exit(1)

    command_main(['learners', opts['<command>']] + opts['<args>'])
