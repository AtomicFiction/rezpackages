name = 'fdk_aac'

version = '0.1.5'

authors = [
    'Fraunhofer IIS <https://www.iis.fraunhofer.de/>'
]
description = \
    '''
    The Fraunhofer FDK AAC Codec Library for Android ("FDK AAC Codec") is
    software that implements the MPEG Advanced Audio Coding ("AAC") encoding and
    decoding scheme for digital audio.  This FDK AAC Codec software is intended to
    be used on a wide variety of Android devices.
    '''

build_requires = [
    'gcc'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7']
]

uuid = 'fdk-aac'

def commands():

    if building:
        env.CPATH.append('{root}/include')
        env.LIBRARY_PATH.append('{root}/lib')
        env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')

