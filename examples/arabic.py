#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import random; random.seed(0)
import webbrowser

import pytagcloud # https://github.com/e9t/PyTagCloud-CJK (not the one in PyPI)

r = lambda: random.randint(0,255)
color = lambda: (r(), r(), r())

tags = [
        {'color': color(), 'tag': u'برچسب ها:', 'size': 100},
        {'color': color(), 'tag': u'کلمات کلیدی', 'size': 70},
        {'color': color(), 'tag': u'فونت میتر', 'size': 50}
       ]

filename = 'arabic.png'
pytagcloud.create_tag_image(tags, filename, fontname='B Mitra', size=(800, 600))
webbrowser.open(filename)
