name = 'pyside'

version = "2-qt5.6"

build_requires = [
    'qt-5.6',
    'python-2.7',
    'cmake-3.10+'
]

requires = [
    'qt-5.6',
    'python-2.7'
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

uuid = "repository.pyside"

def commands():
    env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/lib64/python2.7/site-packages')

