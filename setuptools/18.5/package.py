# -*- coding: utf-8 -*-

name = 'setuptools'

version = '18.5'

tools = [
    'easy_install'
]

build_requires = [
    'python-2.7'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'python-2.7'],
    ['platform-osx', 'arch-x86_64', 'python-2.7']
]


def commands():
    env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/python')


uuid = 'repository.setuptools'
