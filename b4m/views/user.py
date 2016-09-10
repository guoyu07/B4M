#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-

from b4m.libs.mongo import Document, StringField


class User(Document):
    email = StringField(required=True)
    nickname = StringField(max_length=50)
    password = StringField(max_length=50)
