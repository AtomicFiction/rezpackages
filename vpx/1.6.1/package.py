name = 'vpx'

version = '1.6.1'

authors = [
    'Google <https://www.webmproject.org>'
]

description = \
    '''
    WebM is an open, royalty-free, media file format designed for the web.

    WebM defines the file container structure, video and audio formats. WebM files
    consist of video streams compressed with the VP8 or VP9 video codecs and audio
    streams compressed with the Vorbis or Opus audio codecs.
    '''

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7']
]

build_requires = [
    'gcc',
    'yasm'
]

uuid = 'vpx'

def commands():

    if building:
        env.CPATH.append('{root}/include')
        env.LIBRARY_PATH.append('{root}/lib')
        env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')

