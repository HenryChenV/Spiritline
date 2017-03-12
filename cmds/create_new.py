#!/usr/bin/env python
# -*- coding=utf-8 -*-
"""
    Create New Content File
    ~~~~~~~~~~~~~~~~~~~~~~~
"""
import os
import click


__author__ = 'Henry Chen'


new_md_template = '''Title: {title}
Date: {date}
Modified: {date}
Tags: {tags}
Slug: {slug}
Authors: {authors}
Summary:
Status: {status}

[TOC]

'''


def unicode2utf8(text):
    if isinstance(text, unicode):
        return text.encode('utf-8')
    return text


def generate_new_md(filename, title, date, tag, slug, author, status):
    with open(filename, 'w') as new_md_fp:
        new_md_fp.write(
            new_md_template.format(
                title=unicode2utf8(title),
                date=unicode2utf8(date),
                tags=unicode2utf8(tag),
                slug=unicode2utf8(slug),
                authors=unicode2utf8(author),
                status=unicode2utf8(status),
            )
        )


def current_time(ctx, args, value):
    if not value:
        from datetime import datetime
        value = datetime.now().strftime('%Y-%m-%d %H:%M')
    return value


def tag_name_parser(ctx, args, value):
    if value:
        return ', '.join(value)
    return ''


def author_name_parser(ctx, args, value):
    if value:
        value = ', '.join(value)
    else:
        value = 'Henry Chen'
    return value


@click.command()
@click.option('--filename', '-f', required=True, type=click.STRING,
              help='filename of content file')
@click.option('--title', '-T', required=False, type=click.STRING, default='',
              help='Title')
@click.option('--date', '-d', required=False, type=click.STRING, default=None,
              callback=current_time, help='Time to create it')
@click.option('--tag', '-t', required=False, type=click.STRING,
              multiple=True, default=[], callback=tag_name_parser,
              help='Tag')
@click.option('--slug', '-s', required=False, type=click.STRING,
              default='', help='Uuid of content')
@click.option('--author', '-A', required=False, type=click.STRING,
              multiple=True, default=[],
              callback=author_name_parser, help='Authors')
@click.option('--status', '-S', required=False,
              type=click.Choice(('draft', 'published')),
              default='draft', help='Status')
def create_new(filename, title, date, tag, slug, author, status):
    """Create New Content
    """
    if not filename.endswith('.md'):
        filename = '%s.md' % filename

    if os.path.exists(filename):
        prompt = '%s is already existed, do you want to overwrite is?[y/N] ' \
                % filename
        choice = raw_input(prompt).lower()
        while 1:
            if choice in ('y', 'yes'):
                generate_new_md(
                    filename, title, date, tag, slug, author, status)
                print 'success, %s was overwrited by new file.' % filename
                break
            elif choice in ('', 'n', 'no'):
                print ('new file was not created because %s'
                       'was existed.') % filename
                break
            else:
                choice = raw_input('choise must in ("y", "n"): ')
    else:
        generate_new_md(filename, title, date, tag, slug, author, status)
        print 'success, %s was created' % filename
