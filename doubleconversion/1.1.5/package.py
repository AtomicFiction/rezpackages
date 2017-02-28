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
    ["platform-linux", "arch-x86_64", "os-Fedora-25"]
]

uuid = "doublconversion"

def commands():
    if building:
        env.DOUBLE_CONVERSION_INCLUDE_DIR = "{root}/include"
        env.LD_LIBRARY_PATH.append("{root}/lib")    
        # env.DOUBLE_CONVERSION_LIBRARY = "{root}/usr/local/lib/libdouble-conversion.so"
