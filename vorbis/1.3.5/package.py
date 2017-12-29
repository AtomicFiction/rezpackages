name = 'vorbis'

version = '1.3.5'

authors = [
    'Xiph.Org Foundation <xiph.org>'
]

description = \
    '''
    Ogg Vorbis is a new audio compression format. It is roughly comparable to other
    formats used to store and play digital music, such as MP3, VQF, AAC, and other
    digital audio formats. It is different from these other formats because it is
    completely free, open, and unpatented.
    '''

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7']
]

build_requires = [
    'gcc',
    'ogg'
]

uuid = 'vorbis'

def commands():

    if building:
        env.CPATH.append('{root}/include')
        env.LIBRARY_PATH.append('{root}/lib')
        env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')
        env.M4PATH.append('{root}/aclocal')

