#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-

from b4m.views.index import IndexView


def add_url_rule(app):
    app.add_url_rule('/', view_func=IndexView.as_view('index'), methods=['GET'])
