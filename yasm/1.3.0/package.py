name = 'yasm'

version = '1.3.0'

authors = [
    'Peter Johnson <peter@tortall.net>',
    'Michael Urman <mu@tortall.net>'
]

description = \
    '''
    Yasm is a complete rewrite of the NASM assembler under the "new" BSD License.
    '''

build_requires = [
    'gcc'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7']
]

tools = [
    'vsyasm',
    'yasm',
    'ytasm'
]

uuid = 'yasm'

def commands():
    env.PATH.append('{root}/bin')
    env.MANPATH.append('{root}/share/man')

    if building:
        env.CPATH.append('{root}/include')
        env.LIBRARY_PATH.append('{root}/lib')

