#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-

import sys
import os
import json

from flask_script import Manager

from b4m import app
from b4m.libs.utility import filter_cofig, set_log

manager = Manager(app, description='just a blog app',
                  with_default_commands=False)
manager.help_args = ('-?', '-h', '--help')


@manager.option('--conf', default=None, help='the config file')
@manager.option('--host', default='localhost', help='host')
@manager.option('--port', default=8084, help='port')
@manager.option('--debug', default=True, help='debug mode')
@manager.option('--log-file', default=os.path.join(app.root_path, 'log.txt'), help='log file')
@manager.option('--log-level', default='debug', help='log level')
def runserver(conf, **config):
    "run server"

    app.config.update(filter_cofig(config))

    if conf is not None:
        with open(conf) as f:
            app.config.update(filter_cofig(json.load(f)))

    if app.config['DEBUG']:
        app.config['LOG_LEVEL'] = 'debug'

    set_log(app.config['LOG_LEVEL'], app.config['LOG_FILE'])

    app.run(app.config['HOST'], app.config['PORT'], app.config['DEBUG'])


@manager.command
def install():
    "install server"

    pass


if __name__ == '__main__':
    manager.run()
