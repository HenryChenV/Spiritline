#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'henry'
SITENAME = u'SpiritLine'
SITEURL = 'http://localhost:8000'
DISQUS_SITENAME = "spiritline"

#PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh_CN'
DEFAULT_DATE_FORMAT = ('%Y-%m-%d (%A) %H:%M')

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'hide'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Github', 'https://github.com/HenryChenV'),
    ('ThreeBook', 'http://threebook.cn'),
    ('Markdown Syntax', 'http://markdown-zh.readthedocs.org/en/latest/'),
)

# Social widget
SOCIAL = (
    ('Weibo', 'http://weibo.com/dulihandong'),
)

# ABOUT ME, not used
ABOUTME = (
    ('Email', 'chen_hanli@163.com'),
    ('QQ', '648667940'),
)

FOUNDATION_FOOTER_TEXT = "Contact me: Henry Chen, Email: chen_hanli@163.com, QQ: 648667940"

DEFAULT_PAGINATION = 10
MD_EXTENSIONS = [
    "extra",
    "toc",
    "headerid",
    "meta",
    "sane_lists",
    "smarty",
    "wikilinks",
    "admonition",
#    "codehilite(guess_lang=False,pygments_style=emacs,noclasses=True)"
    'codehilite(css_class=highlight,linenums=False)',
]

CNZZ_ANALYTICS = True
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

# Theme
#THEME = "themes/new-bootstrap2"
THEME = "themes/new-foundation-default-colours"
#THEME = "themes/notmyidea"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ["plugins", ]
PLUGINS = ["better_codeblock_line_numbering"]

# Static Files
STATIC_PATHS = ['images']
