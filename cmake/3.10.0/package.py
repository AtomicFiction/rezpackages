name = 'cmake'

version = '3.10.0'

authors = [
    'Kitware <www.kitware.com>'
]

description = \
    '''
    CMake is an extensible, open-source system that manages the build process
    in an operating system and in a compiler-independent manner.
    '''

build_requires = [
    'gcc-4.8.2+'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7']
]

tools = [
    'cmake',
    'ccmake',
    'cpack',
    'ctest'
]

uuid = 'cmake'

def commands():
    env.PATH.prepend('{root}/bin')
    env.CMAKE_MODULE_PATH.append('{root}/share/cmake-3.10/Modules')

    if building:
        env.CPATH.append('{root}/share/cmake-3.10/include')
        env.M4PATH.append('{root}/share/aclocal')

