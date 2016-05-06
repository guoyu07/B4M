#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-

from flask import Flask

from b4m.views import add_url_rule


app = Flask(__name__, static_folder=None)

add_url_rule(app)
