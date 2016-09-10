#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-

from flask import request

from b4m.views.base import BaseView


class IndexView(BaseView):
    def dispatch_request(self):
        print(request.headers, request.environ, request.remote_addr)
        return self.render_template('index.html', title='Hello, World!')
