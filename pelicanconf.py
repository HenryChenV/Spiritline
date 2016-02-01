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
#DEFAULT_DATE_FORMAT = ('%Y-%m-%d (%A) %H:%M')
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')

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
    ('Pelican 中文文档', 'http://pelican-docs-zh-cn.readthedocs.org/en/latest/'),
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
#    "codehilite(guess_lang=False,pygments_style=emacs,noclasses=True)"
    'codehilite(css_class=highlight,linenums=False)',
]

CNZZ_ANALYTICS = True
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

# Theme
THEME = "themes/new-foundation-default-colours"
#THEME = "themes/pelican-bootstrap3"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ["plugins", ]
PLUGINS = ["better_codeblock_line_numbering", ]

# Static Files
STATIC_PATHS = ['images']

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
DISPLAY_BREADCRUMBS = True
SUMMARY_MAX_LENGTH = 15

###################### for theme plumage #########################
#LEFT_SIDEBAR = "left sidebar"
#MENUITEMS = (
#    ("item1", "#"),
#    ("item2", "#"),
#)
#SITESUBTITLE = "site subtitle"
#TIPUE_SEARCH = True
###################### end #######################################


###################### SIDEBAR = "sidebar.html" #########################
#SITESUBTITLE ='Sub-title that goes underneath site name in jumbotron.'
#SITETAG = "Text that's displayed in the title on the home page."

# Extra stylesheets, for bootstrap overrides or additional styling.
#STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css",)

# Put taglist at end of articles, and use the default
# sharing button implementation.
#CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
#CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"

# Default sidebar template. Omit
# this setting for single column
# mode without sidebar.
#SIDEBAR = "sidebar.html"
#########################################################################

########################## for theme chameleon ###########################
#AUTHORS = {
#    u'jack': '/about.html',
#    u'mary': 'http://mary.info',
#    u'tony': 'http://tony.me',
#}
#MENUITEMS = [
#    ('Home', '/'),
#    ('Archives', [
#        ('Tags', '/tags.html'),
#        ('Categories', '/categories.html'),
#        ('Chronological', '/archives.html'),
#    ]),
#    ('Social', [
#        ('Email', 'mailto: maurelinus@stoic.edu'),
#        ('Github', 'http://url-to-github-page'),
#        ('Facebook', 'http://url-to-facebook-page'),
#    ]),
#]
#########################################################################
