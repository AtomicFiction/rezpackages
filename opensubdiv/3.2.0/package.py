
name = "opensubdiv"

version = "3.2.0"

build_requires = [
    'tbb-4',
    'glfw-3'
]

requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

uuid = "opensubdiv"

def commands():

    if building:
        env.OPENSUBDIV_INCLUDE_DIR = '{root}/include'
        env.OPENSUBDIV_ROOT_DIR = '{root}'
        env.LD_LIBRARY_PATH.append('{root}/lib')


