# -*- coding=utf-8 -*-
"""
    Command Line Tools
    ~~~~~~~~~~~~~~~~~~
"""
import click
from .create_new import create_new


@click.group(name='sp_cmds')
def cmds():
    pass


@click.command()
def hello():
    """instruction
    """
    pass
# cmds.add_command(hello)


cmds.add_command(create_new)
