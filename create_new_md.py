#!/usr/bin/env python
#-*- coding=utf-8 -*-
"""
create new md file
"""

__author__ = 'Henry Chen'

import sys
import os
from datetime import datetime

new_md_template = '''Title:
Date: {date}
Modified: {date}
Tags:
Slug: {slug}
Authors: {author}
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


def create_new_md(filename, date, author, status):
    if os.path.exists(filename):
        prompt = '%s is already existed, do you want to overwrite is?[y/N] ' \
                % filename
        choice = raw_input(prompt).lower()
        while 1:
            if choice in ('y', 'yes'):
                generate_new_md(filename, date, author, status)
                print 'success, %s was created' % filename
                break
            elif choice in ('', 'n', 'no'):
                print 'new file was not created because %s was existed.' % filename
                break
            else:
                choice = raw_input('choise must in ("y", "n"): ')



if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except Exception:
        print 'Usage: %s path-to-new-md [status]' % __file__
        sys.exit(1)

    base_filename = os.path.basename(filename)
    slug = base_filename.rstrip('.md') if base_filename.endswith('.md') else base_filename

    now = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M')

    status = 'published'
    if len(sys.argv) >= 3 and sys.argv[2] in ('drafted', 'published'):
        status = sys.argv[2]

    author = __author__

    create_new_md(filename, now, author, status)
