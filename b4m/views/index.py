#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-


from b4m.views.base import BaseView


class IndexView(BaseView):
    def dispatch_request(self):
        return self.json({'context': 'Hello, World!'}, 404, {'X-TEST-HEADER': '1'})
