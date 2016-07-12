#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-

from flask import Flask

from b4m.views import add_url_rule


class B4M(Flask):
    def __init__(self, *args, **kwargs):
        super(B4M, self).__init__(*args, **kwargs)


app = B4M(__name__, static_folder=None)

add_url_rule(app)
