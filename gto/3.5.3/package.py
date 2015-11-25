name = "gto"

version = "3.5.3"

authors = [
    "Tweak Software"
]

description = \
    """
    GTO Python Library
    """

requires = [
]

build_requires = [
    "gcc-4.1.2", 
    "python-2.7"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-6.5"]
]

tools = [
]

uuid = "repository.gto"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append('{root}/python/lib/python2.7/site-packages')

    if building:
        env.GTO_INCLUDE_DIR = "{root}/include"
