#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-

from flask.views import View
from flask import render_template


class IndexView(View):
    def dispatch_request(self):
        return render_template('index.html')
