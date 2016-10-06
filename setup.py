#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-

from setuptools import setup, find_packages


setup(
    name='B4M',

    version='0.1.dev1',

    description='A simple blog designed for myself',

    url='https://github.com/jat001/B4M',

    author='Jat',
    author_email='chat@jat.email',

    license='GPLv3+',

    classifiers=[
        'Development Status :: 1 - Planning',

        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
    ],

    packages=find_packages(),

    install_requires=['Flask', 'Flask-Script', 'mongoengine', 'redis', 'cryptography'],

    test_suite='nose.collector',
    tests_require=['nose']
)
