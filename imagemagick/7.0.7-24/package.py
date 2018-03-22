name = 'imagemagick'

version = '7.0.7-24'

authors = [
    'ImageMagick Studio LLC'
]

description = \
    '''
    Command line image manipulation library and tools.
    '''

build_requires = [
    'gcc-4.8+',
    'openexr'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7']
]

tools = [
    'magick',
    'magick-script',
    'animate',
    'compare',
    'composite',
    'conjure',
    'convert',
    'display',
    'identify',
    'import',
    'mogrify',
    'montage',
    'stream'
]

uuid = 'imagemagick'

def commands():
    env.MAGICK_CONFIGURE_PATH.prepend('{root}/etc/ImageMagick-7')
    env.PATH.append('{root}/bin')
    env.MANPATH.append('{root}/share/man')

    if building:
        env.CPATH.append('{root}/include')
        env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')
        env.LIBRARY_PATH.append('{root}/lib')
