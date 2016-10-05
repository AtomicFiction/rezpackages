name = "automake"

version = "1.15"

authors = [
    "GNU"
]

description = \
    """
    Automake
    """

build_requires = [    
    "autoconf-2.69"
]

variants = [
    ["platform-osx", "arch-x86_64"]
]

tools = [    
]

uuid = "repository.automake"

def commands():
    env.PATH.append("{root}/bin")    

    if building:        
        env.ACLOCAL_PATH = '{root}/share'
