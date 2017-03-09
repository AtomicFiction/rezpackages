name = "gcc"

version = "6.3.1"

authors = [
    "GNU"
]

description = \
    """
    GNU project C and C++ compiler.
    """

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

tools = [
    "gcc",
    "g++",
    "c++",
    "cpp",
    "gcc-ar",
    "gcc-ranlib",
    "gfortran",
    "gcc-nm",
    "gcov"
]

uuid = "gcc"

def commands():
    if building:
        env.CC = "/usr/bin/gcc"
        env.CXX = "/usr/bin/g++"
