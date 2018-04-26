name = "openvdb"

version = "5.1.0"

authors = [
    "DreamWorks Studios"
]

description = \
    """
    OpenVDB is an Academy Award-winning open-source C++ library comprising a novel hierarchical data structure and a suite of tools for the efficient storage and manipulation of sparse volumetric data discretized on three-dimensional grids. It is developed and maintained by DreamWorks Animation for use in volumetric applications typically encountered in feature film production.
    """

private_build_requires = [
    "gcc-4.8.2+"
]

requires = [
    "openexr-2.2.0",
    "tbb"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

uuid = "repository.openvdb"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if building:
        env.LIBRARY_PATH.append("{root}/lib")
        env.CPATH.append("{root}/include")

