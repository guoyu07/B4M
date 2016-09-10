#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-

from b4m.views.index import IndexView
from b4m.views.base import StaticView


def add_url_rule(app):
    app.add_url_rule('/', view_func=IndexView.as_view('index'), methods=['GET'])
    app.add_url_rule('/static/<path:filename>', view_func=StaticView.as_view('static'), methods=['GET'])
