name = "pyilmbase"

version = "2.2.0"

authors = [
    "ILM"
]

description = \
    """
    Python bindings for the utility libraries from ILM used by OpenEXR.
    """

build_requires = [
    "gcc-4.8.2+",
    "python-2.7",
    "boost-1.55",
    "ilmbase-2.2.0"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7", "python-2.7"]
]

uuid = "repository.pyilmbase"

def commands():
    env.PYTHONPATH.append("{root}/lib64/python2.7/site-packages")

    if building:
        env.CPATH.append('{root}/include')
        env.LIBRARY_PATH.append('{root}/lib')
        env.M4PATH.append('{root}/share/aclocal')
        env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')

