#!/usr/bin/env python

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

required =[
'flask',
'flask_restful',
'requests',
'sqlalchemy',
'mysqlclient'
]



setup(
    name='chatroom',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/joanff/chatroom',
    author='Yang Fan',
    author_email='joanff@qq.com',
    install_requires= required,
)
