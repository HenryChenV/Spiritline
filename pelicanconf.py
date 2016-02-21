#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'henry'
SITENAME = u"Henry's SpiritLine"
SITEURL = 'http://localhost:8000'
DISQUS_SITENAME = "spiritline"

#PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh_CN'
#DEFAULT_DATE_FORMAT = ('%Y-%m-%d (%A) %H:%M')
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'Essay'
IGNORE_FILES = ['template.md']

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
    ('Pelican 中文文档', 'http://pelican-docs-zh-cn.readthedocs.org/en/latest/'),
)

# Social widget
SOCIAL = (
    ('Weibo', 'http://weibo.com/dulihandong'),
)

DEFAULT_PAGINATION = 5
MD_EXTENSIONS = [
    "extra",
    "toc",
    "headerid",
    "meta",
    "sane_lists",
    "smarty",
    "wikilinks",
    "admonition",
#    "nl2br",
#    "codehilite(guess_lang=False,pygments_style=emacs,noclasses=True)"
    "codehilite(css_class=highlight,linenums=False)",
    "mdx_del_ins",
]

CNZZ_ANALYTICS = True
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/index.html'

# Theme
THEME = "themes/new-foundation-default-colours"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ["plugins", ]
PLUGINS = ["better_codeblock_line_numbering", "tag_cloud"]

# Static Files
STATIC_PATHS = ['images']

DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_TAGS_INLINE = True
DISPLAY_BREADCRUMBS = True
SUMMARY_MAX_LENGTH = 15

# configurations of foundation-default-colours
# the front page will show full articles instead of summaries + links to the
# full articles
FOUNDATION_FRONT_PAGE_FULL_ARTICLES = False
# Google Droid fonts will be used instead of the default Open Sans font that
# ships with Foundation
FOUNDATION_ALTERNATE_FONTS = True
# a tag list will appear in the mobile sidebar. However note that if you have a
# lot of tags, this list may get rather long and unweildly
FOUNDATION_TAGS_IN_MOBILE_SIDEBAR = False
# If you wish to use the newer Google Analytics embed code, enable
# FOUNDATION_NEW_ANALYTICS and set the FOUNDATION_ANALYTICS_DOMAIN to the
# Google-Analytics-supplied name for your code block
FOUNDATION_NEW_ANALYTICS = False
FOUNDATION_ANALYTICS_DOMAIN = ''
# change the footer text
FOUNDATION_FOOTER_TEXT = "".join(
    (
        "Contact me: Henry Chen, ",
        "Email: <a href='mailto:chen_hanli@163.com'>chen_hanli@163.com</a>, ",
        "QQ: 648667940",
    )
)

# themes that Pygments provides
# autumn borland bw colorful default emacs friendly fruity manny monokai
# murphy native pastie perldoc tango trac vs
FOUNDATION_PYGMENT_THEME = 'monokai'


# custom
# ABOUT ME, not used
ABOUTME = (
    ('Email', 'chen_hanli@163.com'),
    ('QQ', '648667940'),
)
INTROS = (
    "The Story Of Me.",
)

# tag cloud
# Count of different font sizes in the tag cloud
TAG_CLOUD_STEPS = 4
# Maximum number of tags in the cloud
TAG_CLOUD_MAX_ITEMS = 100
# The tag cloud ordering scheme.
# Valid values: random, alphabetically, alphabetically-rev, size and size-rev
TAG_CLOUD_SORTING = "random"
# Optionnal setting : can bring **badges**,
# which mean say : display the number of each tags present on all articles
TAG_CLOUD_BADGE = True
