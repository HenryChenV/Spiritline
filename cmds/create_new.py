#!/usr/bin/env python
#-*- coding=utf-8 -*-
"""
create new md file
"""

__author__ = 'Henry Chen'

import os
import argparse
import click
from datetime import datetime

new_md_template = '''Title:
Date: {date}
Modified: {date}
Tags:
Slug: {slug}
Authors: {author}
Summary:
Status: {status}

[TOC]

'''


def generate_new_md(filename, date, author, status):
    with open(filename, 'w') as new_md_fp:
        new_md_fp.write(
            new_md_template.format(
                date=date,
                slug=slug,
                author=author,
                status=status
            )
        )


@click.option('--filename', '-f', required=True, type=click.STRING,
              help='filename of content file')
@click.option('--date')
def create_new(filename, date, author, status):
    if not filename.endswith('.md'):
        filename = '%s.md' % filename

    if os.path.exists(filename):
        prompt = '%s is already existed, do you want to overwrite is?[y/N] ' \
                % filename
        choice = raw_input(prompt).lower()
        while 1:
            if choice in ('y', 'yes'):
                generate_new_md(filename, date, author, status)
                print 'success, %s was overwrited by new file.' % filename
                break
            elif choice in ('', 'n', 'no'):
                print ('new file was not created because %s'
                       'was existed.') % filename
                break
            else:
                choice = raw_input('choise must in ("y", "n"): ')
    else:
        generate_new_md(filename, date, author, status)
        print 'success, %s was created' % filename


def parse_args():
    parser = argparse.ArgumentParser(description="Create New Markdown File.")

    parser.add_argument('path',
                        metavar='path',
                        help="path to md file")
    parser.add_argument('-s',
#                        metavar='--status',
                        dest='status',
                        default='published',
                        choices=('draft', 'published'),
                        help='the status of post (draft or published)')
    parser.add_argument('--slug',
                        dest='slug',
                        help='the slug of post.')

    args = parser.parse_args()
    path, slug, status = args.path, args.slug, args.status
    if not slug:
        base_filename = os.path.basename(path)
        if not base_filename:
            raise ValueError("Invalid Path.")
        slug = base_filename.rstrip(
            '.md') if base_filename.endswith('.md') else base_filename

    return path, slug, status


if __name__ == '__main__':

    path, slug, status = parse_args()
    now = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M')

    create_new(path, now, __author__, status)
