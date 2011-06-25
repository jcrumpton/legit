# -*- coding: utf-8 -*-

"""
legit.cli
~~~~~~~~~

This module povides the CLI interface to legit.
"""

import sys

from clint import args
from clint.eng import join as eng_join
from clint.textui import colored, indent, puts

from .core import (
    get_available_branches, get_current_branch,
     __version__
)




def main():

    if args.get(0) in cmd_map:

        arg = args.get(0)
        args.remove(arg)

        cmd_map.get(arg).__call__(args)
        sys.exit()

    elif args.contains(('-h', '--help')):
        display_info()
        sys.exit(1)

    elif args.contains(('-v', '--version')):
        display_version()
        sys.exit(1)

    else:
        display_info()
        sys.exit(1)



def cmd_switch(args):
    to_branch = args.get(0)

    if not to_branch:
        print 'Available branches:'

        current_branch = get_current_branch()

        for branch in get_available_branches():
            if current_branch == branch:
                print ' + {0}'.format(colored.yellow(branch))
            else:
                print ' - {0}'.format(colored.yellow(branch))

        sys.exit()

    if to_branch not in get_available_branches():
        print 'Branch not found.'
    else:
        print 'stash and dash.'



def display_info():
    puts('{0} by Kenneth Reitz <me@kennethreitz.com>'.format(colored.yellow('legit')))
    puts('https://github.com/kennethreitz/legit\n')
    puts('Usage: {0}'.format(colored.blue('legit <command>')))
    puts('Commands: {0}.\n'.format(
        eng_join(
            [str(colored.green(c)) for c in sorted(cmd_map.keys())]
        )
    ))


def display_version():
    puts('{0} v{1}'.format(
        colored.yellow('legit'),
        __version__
    ))




cmd_map = dict(
    switch=cmd_switch,
    sync=cmd_switch,
    branch=cmd_switch,
    publish=cmd_switch,
    unpublish=cmd_switch
)