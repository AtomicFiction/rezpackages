name = "doubleconversion"

version = "1.1.5"

authors = [
    ""
]

description = \
    """
    """

build_requires = [
    "scons"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

uuid = "doublconversion"

def commands():
    if building:
        env.CPATH.append("{root}/include")
        env.LD_LIBRARY_PATH.append("{root}/lib")
