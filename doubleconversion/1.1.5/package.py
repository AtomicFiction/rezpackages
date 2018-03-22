name = "doubleconversion"

version = "1.1.5"

authors = [
    'Google Inc.',
    'Mozilla Foundation',
    'Jeff Muizelaar <jmuizelaar@mozilla.com>',
    'Mike Hommey <mhommey@mozilla.com>',
    'Martin Olsson <mnemo@minimum.se>',
    'Kent Williams <chaircrusher@gmail.com>',
    'Elan Ruusamae <glen@delfi.ee>'
]

description = \
    """
    Efficient binary-decimal and decimal-binary conversion routines for IEEE
    doubles.
    """

private_build_requires = [
    "scons"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

uuid = "doublconversion"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.CPATH.append("{root}/include")
        env.LIBRARY_PATH.append("{root}/lib")
