name = 'setuptools'

version = '38.2.4'

authors = [
    'Python Packaging Authority'
]

description = \
    '''
    Easily download, build, install, upgrade, and uninstall Python packages
    '''

tools = [
    'easy_install'
]

requires = [
    'python-2.7'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7', 'python-2.7'],
]

uuid = 'setuptools'

def commands():
    env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/python2.7/site-pacakges')

