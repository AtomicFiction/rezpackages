name = "pyside"

version = "1.2.4"

build_requires = [
    'shiboken-1.2.4',    
    'qt-4.8',    
    'python-2.7'
]

requires = [    
    'shiboken-1.2.4',
    'qt-4.8',
    'python-2.7'
]

variants = [
    ["platform-linux", "arch-x86_64"]
]

uuid = "repository.pyside"

def commands():
    env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')
    env.LD_LIBRARY_PATH.append('{root}/lib')
    
    if building:        
        env.SHIBOKEN_INCLUDE_DIR = '{root}/include'

        
