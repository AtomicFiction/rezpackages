name = "shiboken"

version = "1.2.4"

build_requires = [
    'qt-4.8',
    'python-2.7'
]

requires = ['python-2.7']

variants = [
    ["platform-linux", "arch-x86_64"]
]

uuid = "repository.shiboken"

def commands():
    env.PATH.append('{root}/bin')
    
    if building:        
        env.SHIBOKEN_INCLUDE_DIR = '{root}/include'
        env.LD_LIBRARY_PATH.append('{root}/lib')
