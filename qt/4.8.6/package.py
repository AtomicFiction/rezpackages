name = "qt"

version = "4.8.6"

build_requires = [    
]

variants = [
    ["platform-linux", "arch-x86_64"],
    ['platform-osx', 'arch-x86_64']
]



def commands():
    env.PATH.append('{root}/bin')
    if building:
        env.QT_HOME = "{root}"
        env.QT_VERSION = "4.8.6"
        env.QT_INCLUDE_DIR = "{root}/include"
        # static libs only, hence build-time only
        env.LD_LIBRARY_PATH.append("{root}/lib")

uuid = "repository.qt"        
