#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-

from b4m.views.base import BaseView


class IndexView(BaseView):
    def dispatch_request(self):
        return self.render_template('index.html', title='Hello, World!')
