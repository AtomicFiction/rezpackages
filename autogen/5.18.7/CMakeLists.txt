CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(package_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url autogen/autogen-${package_version}.tar.gz
    http://ftp.gnu.org/gnu/autogen/autogen-${package_version}.tar.gz
)

set(CMAKE_VERBOSE_MAKEFILE ON)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)
set(make_args "")

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    autogen
    URL ${url}
    PREFIX autogen
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND ${install_cmd}
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make ${make_args}
)
