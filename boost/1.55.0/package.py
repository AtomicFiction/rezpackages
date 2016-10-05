name = 'boost'

version = '1.55.0'

authors = [
    'boost.org'
]

description = \
    '''
    Peer-reviewed portable C++ source libraries.
    '''

build_requires = [
    'python-2.7'
]

variants = [
    ['platform-linux', 'arch-x86_64'],
    ['platform-osx', 'arch-x86_64']
]


def commands():
    if building:
        env.BOOST_ROOT = '{root}'
        env.BOOST_INCLUDE_DIR = '{root}/include'

        # static libs
        env.LD_LIBRARY_PATH.append('{root}/lib')

uuid = 'repository.boost'
