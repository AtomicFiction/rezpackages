name = "tbb"

version = "2017_U6"

authors = [
    "Intel"
]

description = \
    """
    Intel(R) Threading Building Blocks (Intel(R) TBB) lets you easily write
    parallel C++ programs that take full advantage of multicore performance, that
    are portable, composable and have future-proof scalability.
    """

build_requires = [
    "gcc-4.8.2+"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

uuid = "repository.tbb"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib/release")

    if building:
        env.CPATH.append("{root}/include")
