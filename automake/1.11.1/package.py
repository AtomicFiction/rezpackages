name = 'automake'

version = '1.11.1'

authors = [
    'GNU'
]

description = \
    '''
    Automake
    '''

build_requires = [
    'autoconf-2'
]

variants = [
    ['platform-osx', 'arch-x86_64']
]

tools = [
]


def commands():
    env.PATH.append('{root}/bin')

    if building:
        env.ACLOCAL_PATH = '{root}/share'

uuid = 'repository.automake'
