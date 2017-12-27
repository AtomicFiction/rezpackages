name = "openimageio"

version = "1.7.11"

authors = [
    "Larry Gritz"
]

description = \
    """
    OpenImageIO is a library for reading and writing images, and a bunch of
    related classes, utilities, and applications.
    """

private_build_requires = [
    'cmake-3.2.2+',
    "boost-1.55",
    "gcc-4.8.2+",
    "ffmpeg-3.4",
    "opencolorio-1.0.9",
    "ilmbase-2.2",
    'openexr-2.2',
    'ptex'
]

requires = [
    'qt-4.8+<5',
    'python-2.7'
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7", "python-2.7"]
]

tools = [
    "iconvert",
    "idiff",
    "igrep",
    "iinfo",
    "maketx",
    "oiiotool"
]

uuid = "openimageio"

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/lib/python/site-packages")

    if building:
        env.OIIO_INCLUDE_DIR = "{root}/include"
        env.LD_LIBRARY_PATH.append("{root}/lib")
