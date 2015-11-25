name = "qt"

version = "4.8.6"

build_requires = [
    "gcc-4.8.2", 
    "python-2.7"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-6.5"]
]

tools = [
]

uuid = "repository.qt-4.8.2"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    
    if building:
        env.GTO_INCLUDE_DIR = "{root}/include"