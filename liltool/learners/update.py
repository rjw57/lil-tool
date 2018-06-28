"""
Usage:
    lil learners update (-h | --help)
    lil learners update <lookup-group>

Options:
    -h, --help              Show a brief usage summary.
    <lookup-group>          Lookup group name.

"""
import logging
import docopt


LOG = logging.getLogger('lil learners update')


def main(argv):
    opts = docopt.docopt(__doc__, argv=argv)
    group = opts['<lookup-group>']
    LOG.info('Fetching membership of lookup group "%s"', group)
