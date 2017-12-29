name = 'pip'

version = '9.0.1'

authors = [
    'The pip developers'
]

description = \
    '''
    The PyPA recommended tool for installing Python packages.
    '''

tools = [
    'pip',
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7', 'python-2.7'],
]

requires = [
    'setuptools',
    'python-2.7'
]

uuid = 'pip'

def commands():

    env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/python')

