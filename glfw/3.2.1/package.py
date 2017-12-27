
name = 'glfw'

version = '3.2.1'

build_requires = [
    'gcc'
]

requires = [
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7']
]

uuid = 'glfw'

def commands():

    if building:
        env.CPATH.append('{root}/include')
        env.CMAKE_MODULE_PATH.append('{root}/lib/cmake')
        env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')
        env.LD_LIBRARY_PATH.append('{root}/lib')

