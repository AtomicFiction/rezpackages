name = "autoconf"

version = "2.69"

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

tools = [ 
   'autoconf',
   'autoheader',
   'autom4te',
   'autoreconf',
   'autoscan',
   'autoupdate',
   'ifnames'
]

uuid = "repository.autoconf"

def commands():
    env.PATH.append("{root}/bin")    

    if building:        
        env.ACLOCAL_PATH = '{root}/share'
