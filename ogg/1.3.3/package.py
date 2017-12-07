name = 'ogg'

version = '1.3.3'

authors = [
    'Xiph.Org Foundation <xiph.org>'
]

description = \
    '''
    The Ogg transport bitstream is designed to provide framing, error protection
    and seeking structure for higher-level codec streams that consist of raw,
    unencapsulated data packets, such as the Opus, Vorbis and FLAC audio codecs or
    the Theora and Dirac video codecs.
    '''

build_requires = [
    'gcc'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7']
]

uuid = 'ogg'

def commands():

    if building:
        env.CPATH.append('{root}/include')
        env.LIBRARY_PATH.append('{root}/lib')
        env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')
        env.M4PATH.append('{root}/aclocal')

