name = 'alembic'

version = '1.6.1'

authors = [
    'Sony Pictures Imageworks, Inc.',
    'Industrial Light and Magic'
]

description = \
    '''
    Alembic is an open framework for storing and sharing scene data that includes a
    C++ library, a file format, and client plugins and applications. 
    '''

private_build_requires = [
    'boost-1.55',
    'maya'
]

build_requires = [
    'gcc-4.8.2+'
]

requires = [
    'openexr-2.2',
    'python-2.7',
    'ilmbase-2.2',
    'hdf5-1.8.12+',
    'pyilmbase-2'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7']
]

tools = [
    'abcconvert',
    'abcdiff',
    'abcecho',
    'abcechobounds',
    'abcls',
    'abcstitcher',
    'abctree'
]

uuid = 'alembic'

def commands():
    env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')
    env.LD_LIBRARY_PATH.append('{root}/lib')

    if building:
        env.CMAKE_MODULE_PATH.append('{root}/lib/cmake')
        env.LIBRARY_PATH.append('{root}/lib')
        env.CPATH.append('{root}/include')
