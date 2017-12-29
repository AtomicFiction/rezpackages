name = 'libtool'

version = '2.4.6'

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

tools = [ ]

uuid = 'repository.libtool'

def commands():
    env.PATH.append('{root}/bin')
