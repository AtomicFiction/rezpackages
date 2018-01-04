name = 'virtualenv'

version = '15.1.0'

authors = [
    'Ian Bicking',
    'Brian Rosner',
    'Carl Meyer',
    'Jannis Leidel',
    'Paul Moore',
    'Paul Nasrat',
    'Marcus Smith'
]

description = \
    '''
    A tool for creating isolated 'virtual' python environments.
    '''

requires = [
    'python-2.7',
    'setuptools',
    'pip',
]

tools = [
    'virtualenv'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7', 'python-2.7'],
]

uuid = 'virtualenv'

def commands():
    env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/python2.7/site-packages')

