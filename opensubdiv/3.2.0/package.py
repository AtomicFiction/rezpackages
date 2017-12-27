
name = "opensubdiv"

version = "3.2.0"

build_requires = [
    'glfw-3'
]

requires = [
    'tbb-4'
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


