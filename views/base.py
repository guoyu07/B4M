#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-

import os

from flask.views import View
from flask import current_app, send_from_directory, render_template, request

from b4m.libs.utility import path_join, safe_path_join


class StaticView(View):
    def dispatch_request(self, filename):
        theme_path = path_join('static')

        if filename[0:7] != 'common/':
            theme_path = path_join('static', current_app.config['THEME'])

            if current_app.config['THEME'] != 'default' and os.path.isfile(safe_path_join(theme_path, filename) is not True):
                theme_path = path_join('static', 'default')

        return send_from_directory(theme_path, filename)


class BaseView(View):
    def render_template(self, template_name_or_list, **context):
        return render_template(template_name_or_list, jss=(
            'common/vue/vue.js',
            'common/vue/vue-resource.js',
        ), is_ajax=request.args.get('is_ajax'), **context)
