name = 'gto'

version = '3.5.3'

authors = [
    'Tweak Software'
]

description = \
    '''
    GTO Python Library
    '''

requires = [
    'python-2.7'
]

build_requires = [
    'gcc-4.8+',
    'python-2.7'
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7", "python-2.7"]
]

tools = [
    'gto2obj',
    'gtofilter',
    'gtoimage',
    'gtoinfo',
    'gtomerge'
]


def commands():
    env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/python/lib64/python2.7/site-packages')
    env.INFOPATH.append('{root}/share/info')

    if building:
        env.CPATH.append('{root}/include')

uuid = 'repository.gto'
