name = "qt"

version = "4.8.6"

authors = [
    "Troltech"
]

build_requires = [
    "gcc-4.8.2+"
]

variants = [
    ["platform-linux", "arch-x86_64", 'os-CentOS-7']
]

uuid = "repository.qt-4.8.6"

def commands():
    env.PATH.append('{root}/bin')

    if building:
        env.QT_HOME = "{root}"
        env.QT_VERSION = "4.8.6"
        env.QT_INCLUDE_DIR = "{root}/include"

        # static libs only, hence build-time only
        env.LD_LIBRARY_PATH.append("{root}/lib")
