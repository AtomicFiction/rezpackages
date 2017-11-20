CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(hdf5_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_hdf5 hdf5/hdf5-${hdf5_version}.tar.gz
    https://www.hdfgroup.org/ftp/HDF5/releases/hdf5-${hdf5_version}/src/hdf5-${hdf5_version}.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    hdf5
    URL ${url_hdf5}
    PREFIX hdf5
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
               -DCMAKE_POSITION_INDEPENDENT_CODE=ON
               -DBUILD_SHARED_LIBS=OFF
               -DHDF5_BUILD_EXAMPLES=OFF
               -DBUILD_TESTING=OFF
               -DHDF5_BUILD_HL_LIB=ON
)
