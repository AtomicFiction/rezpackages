name = "opencolorio"

version = "1.0.9"

authors = [
    "Sony Imageworks"
]

description = \
    """
    OpenColorIO Color Management Framework
    """

build_requires = [
    "boost-1.55",
    "gcc-4.8.2+",
    "python-2.7"

]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7", "python-2.7"]
]

tools = [
    "ociobacklut",
    "ociocheck"
]

uuid = "opencolorio"

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.CPATH.append("{root}/include")
        env.LIBRARY_PATH.append("{root}/lib")
        env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')

