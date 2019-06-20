name = "boost"

version = "1.66.0"

authors = [
    "boost.org"
]

description = \
    """
    Peer-reviewed portable C++ source libraries.
    """

build_requires = [
    "gcc-4.8.2+",
    'python-2.7+'
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7", "python-2.7"]
]

uuid = "repository.boost"

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.CPATH.append("{root}/include")
        env.LIBRARY_PATH.append("{root}/lib")
