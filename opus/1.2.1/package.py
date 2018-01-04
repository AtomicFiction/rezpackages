name = 'opus'

version = '1.2.1'

authors = [
    'Xiph.Org Foundation <xiph.org>'
]

description = \
    '''
    Opus is a totally open, royalty-free, highly versatile audio codec.
    '''

build_requires = [
    'gcc'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7']
]

uuid = 'opus'

def commands():

    if building:
        env.CPATH.append('{root}/include')
        env.CPATH.append('{root}/include/opus')
        env.LIBRARY_PATH.append('{root}/lib')
        env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')
        env.M4PATH.append('{root}/aclocal')

