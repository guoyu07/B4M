#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-

from flask import jsonify
from flask.views import View


class BaseView(View):
    def json(self, response, status, headers):
        # Why it works? See make_response in app.py. fuck the document.
        return jsonify(**response), status, headers
