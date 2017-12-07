name = 'ffmpeg'

version = '3.4'

authors = [
    'FFmpeg Team'
]

description = \
    '''
    FFmpeg is the leading multimedia framework, able to decode, encode, transcode,
    mux, demux, stream, filter and play pretty much anything that humans and
    machines have created.
    '''

build_requires = [
    'gcc',
    'yasm',
    'x264',
    'x265', # not enabled
    'fdk_aac',
    'lame',
    'opus', # not enabled
    'vorbis', # not enabled
    'vpx'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7']
]

tools = [
    'ffmpeg',
    'ffserver',
    'ffprobe',
]

uuid = 'ffmpeg'

def commands():
    env.PATH.append('{root}/bin')
    env.MANPATH.append('{root}/share/man')

    if building:
        env.CPATH.append('{root}/include')
        env.LIBRARY_PATH.append('{root}/lib')
        env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')
