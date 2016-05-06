#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-

import os

from flask import send_from_directory

from b4m.views.index import IndexView
from b4m.libs.utility import path_join, safe_path_join


def add_url_rule(app):
    app.add_url_rule('/', view_func=IndexView.as_view('index_view'))

    @app.route('/static/<path:filename>')
    def static(filename):
        theme_path = path_join('static', app.config['THEME'])

        if not os.path.isfile(safe_path_join(theme_path, filename)):
            theme_path = path_join('static', 'default')

        return send_from_directory(theme_path, filename)
