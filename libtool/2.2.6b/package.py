name = "libtool"

version = "2.2.6b"

authors = [
    "GNU"
]

description = \
    """
    Autoconf
    """

build_requires = [    
]

variants = [
    ["platform-osx", "arch-x86_64"]
]

tools = [ ]

uuid = "repository.libtool"

def commands():
    env.PATH.append("{root}/bin")
    env.ACLOCAL_PATH.append("{root}/share/aclocal")
