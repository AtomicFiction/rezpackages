name = "scons"

version = "2.5.1"

authors = [
    ""
]

description = \
    """
    """

build_requires = [
    "python-2.7"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7", "python-2.7"]
]

uuid = "scons"

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
