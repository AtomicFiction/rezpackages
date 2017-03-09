
name = "ptex"

version = "2.0.30"

build_requires = [
    'gcc-4.8.2+'
]

requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

uuid = "ptex"

def commands():
    env.PATH.append("{root}/bin")

    if building:
        env.PTEX_INCLUDE_DIR = '{root}/include'
        env.PTEX_LOCATION = '{root}'
        env.LD_LIBRARY_PATH.append('{root}/lib')


