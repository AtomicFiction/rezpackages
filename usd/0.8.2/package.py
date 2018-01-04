name = 'usd'

version = '0.8.2'

authors = [
    'Pixar Animation Studios'
]

description = \
    '''
    Universal Scene Description (USD) is an efficient, scalable system for
    authoring, reading, and streaming time-sampled scene description for
    interchange between graphics applications.
    '''

build_requires = [
    'gcc',
    'cmake-3.1+',
]

requires = [
    'alembic',
    'boost-1.55+',
    'hdf5-1.8.11+',
    'houdini-16',
    'ilmbase-2.2.0',
    'katana-2.5+',
    'maya-2016EXT2+',
    'openexr-2.2.0',
    'openimageio-1.5.11+',
    'opensubdiv-3.0.5+',
    'ptex-2.0.30',
    'pyopengl-3.1.0',
    'pyside-1.2.4',
    'python-2.7',
    'tbb-4.3.1'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7']
]

uuid = 'usd'

def commands():
    env.PYTHONPATH.append('{root}/lib/python')
    env.PATH.append('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib')

    if 'maya' in request:
        env.MAYA_PLUG_IN_PATH.append('{root}/third_party/maya/plugin')
        env.MAYA_SCRIPT_PATH.append('{root}/third_party/maya/share/usd/plugins/usdMaya/resources')

    if 'katana' in request:
        env.KATANA_RESOURCES.append('{root}/third_party/katana/plugin')
        env.KATANA_POST_PYTHONPATH.append('{root}/third_party/katana/lib')

    if 'houdini' in request:
        env.HOUDINI_PATH.append('{root}/third_party/houdini')

    if building:
        env.CPATH.append('{root}/include')
        env.CMAKE_MODULE_PATH.append('{root}')
        env.CMAKE_MODULE_PATH.append('{root}/cmake')


