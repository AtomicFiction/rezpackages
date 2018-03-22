name = 'x264'

version = '20171123-2245-stable'

authors = [
    'Alex Izvorski <aizvorski@gmail.com>',
    'Alex Wright <alexw0885@gmail.com>',
    'bobololo',
    'Christian Heine <sennindemokrit@gmx.net>',
    'David Wolstencroft',
    'Eric Petit <eric.petit@lapsus.org>',
    'Fiona Glaser <fiona@x264.com>',
    'Gabriel Bouvigne <bouvigne@mp3-tech.org>',
    'Guillaume Poirier <gpoirier@mplayerhq.hu>',
    'Henrik Gramner <henrik@gramner.com>',
    'Laurent Aimar <fenrir@videolan.org>',
    'Loren Merritt <pengvado@akuvian.org>',
    'Mans Rullgard <mru@mansr.com>',
    'Michael Niedermayer <michaelni@gmx.at>',
    'Mike Matsnev <mike@po.cs.msu.su>',
    'Min Chen <chenm001@163.com>',
    'Radek Czyz <radoslaw@syskin.cjb.net>'
]

description = \
    '''
    x264 is a free software library and application for encoding video streams into
    the H.264/MPEG-4 AVC compression format, and is released under the terms of the
    GNU GPL.
    '''

build_requires = [
    'gcc',
    'yasm'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7']
]

tools = [
    'x264'
]

uuid = 'x264'

def commands():
    env.PATH.append('{root}/bin')

    if building:
        env.CPATH.append('{root}/include')
        env.LIBRARY_PATH.append('{root}/lib')
        env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')

