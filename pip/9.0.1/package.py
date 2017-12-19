name = 'pip'

version = '9.0.1'

tools = [
    'pip',
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7', 'python-2.7'],
]

requires = [
    'setuptools-18.5',
    'python-2.7'
]


def commands():
    env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/python')


uuid = 'pip'
