name = 'x265'

version = '2.6'

authors = [
    'MulticoreWare <https://multicorewareinc.com/>'
]

description = \
    '''
    x265 is a H.265 / HEVC video encoder application library, designed to
    encode video or images into an H.265 / HEVC encoded bitstream.
    '''

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7']
]

build_requires = [
    'gcc',
    'yasm'
]

tools = [
    'x265'
]

uuid = 'x265'

def commands():
    env.PATH.append('{root}/bin')

    if building:
        env.CPATH.append('{root}/include')
        env.LIBRARY_PATH.append('{root}/lib')
        env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')

