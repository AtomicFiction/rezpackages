name = "pyside_tools"

version = "0.2.15"

authors = [
    'PySide developers',
    'Torsten Marek',
    'Phil Thompson',
    'Trolltech',
    'Phil Thompson'
]

descriptions = \
    '''
    PySide development tools (pyuic and pyrcc)
    '''

requires = [
    'shiboken-1.2.4',
    'qt-4.8',
    'python-2.7',
    'pyside-1.2.4'
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

uuid = "repository.pyside-tools"

def commands():
    env.PATH.prepend('{root}/bin')
    env.PYTHONPATH.append('{root}/lib64/python2.7/site-packages')
    env.MANPATH.append('{root}/share/man')
