name = 'autoconf'

version = '2.63'

authors = [
    'GNU'
]

description = \
    '''
    Autoconf
    '''

build_requires = [
]

variants = [
    ['platform-osx', 'arch-x86_64']
]

tools = [
    'autoconf',
    'autoheader',
    'autom4te',
    'autoreconf',
    'autoscan',
    'autoupdate',
    'ifnames'
]


def commands():
    env.PATH.append('{root}/bin')

    if building:
        env.ACLOCAL_PATH = '{root}/share'

uuid = 'repository.autoconf'
