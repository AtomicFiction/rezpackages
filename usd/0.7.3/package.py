
name = "usd"

version = "0.7.3"

build_requires = [
    'python-2.7',
    'boost-1.55',
    'openexr-2.2.0',
    'doubleconversion-1.1',
    'tbb-4.4',
    'opensubdiv-3.0.5+',
    'openimageio-1.5.11+',
    'ptex-2.0.30',
    #'pyside-1.2',
    'PyOpenGL-3.1.0'
]

requires = [
    'python-2.7',
    #'pyside-1.2',
    'PyOpenGL',
]

variants = [
    ["platform-linux", "arch-x86_64", "os-Fedora-25", 'python-2.7']
]

uuid = "usd"

def commands():
    env.PYTHONPATH.append('{root}/lib/python')
    env.PATH.append('{root}/bin')
    env.MAYA_PLUG_IN_PATH.append('{root}/third_party/maya/plugin')
    env.MAYA_SCRIPT_PATH.append('{root}/third_party/maya/share/usd/plugins/usdMaya/resources')

    if building:
        env.USD_INCLUDE_DIR = '{root}/include'
        env.LD_LIBRARY_PATH.append('{root}/lib')


