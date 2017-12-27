name = "shiboken"

version = "1.2.4"

authors = [
    'John Cummings <jcummings2@users.sf.net>',
    'John Ehresman <jpe@wingware.com>',
    'Roman Lacko <backup.rlacko@gmail.com>',
    'Matthew Woehlke <matthew.woehlke@kitware.com>',
    'Anderson Lizardo <anderson.lizardo@openbossa.org>',
    'Bruno Araujo <bruno.araujo@openbossa.org>',
    'Hugo Parente Lima <hugo.lima@openbossa.org>',
    'Lauro Moura <lauro.neto@openbossa.org>',
    'Luciano Wolf <luciano.wolf@openbossa.org>',
    'Marcelo Lira <marcelo.lira@openbossa.org>',
    'Renato Araujo Oliveira Filho <renato.filho@openbossa.org>'
]

description = \
    '''
    Python bindings generator that uses API Extractor and outputs CPython code.
    '''

requires = [
    'qt-4.8',
    'python-2.7'
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

uuid = "repository.shiboken"

def commands():
    env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/lib64/python2.7/site-packages')
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.MANPATH.append('{root}/share/man')

    if building:
        env.CPATH.append('{root}/include')
        env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')
        env.CMAKE_MODULE_PATH.append('{root}/lib/cmake/Shiboken-{version}')

