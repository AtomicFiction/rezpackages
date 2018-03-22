name = 'lame'

version = '3.100'

authors = [
    'Robert Hegemann',
    'Alexander Leidinger',
    'Rogerio Brito'
]

description = \
    '''
    LAME is a high quality MPEG Audio Layer III (MP3) encoder licensed under the LGPL.
    '''

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7']
]

build_requires = [
    'gcc',
    'yasm'
]

tools = [
    'lame'
]

uuid = 'lame'

def commands():
    env.PATH.append('{root}/bin')
    env.MANPATH.append('{root}/share/man')

    if building:
        env.CPATH.append('{root}/include')
        env.LIBRARY_PATH.append('{root}/lib')

