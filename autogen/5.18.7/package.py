name = "autogen"

version = "5.18.7"

authors = [
    "GNU"
]

description = \
    """
    Autogen
    """

build_requires = [    
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
