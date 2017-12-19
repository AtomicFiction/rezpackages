CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(cmake_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_cmake cmake/cmake-${cmake_version}.tar.gz
    https://cmake.org/files/v3.10/cmake-${cmake_version}.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    cmake
    URL ${url_cmake}
    PREFIX cmake
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./bootstrap --prefix=${CMAKE_INSTALL_PREFIX} --parallel=$ENV{REZ_BUILD_THREAD_COUNT}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make ${make_args}
)
