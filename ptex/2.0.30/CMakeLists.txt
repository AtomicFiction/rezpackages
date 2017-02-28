CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(ptex_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_ptex ptex/ptex-${ptex_version}.tar.gz
    https://github.com/wdas/ptex/archive/v${ptex_version}.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    ptex
    URL ${url_ptex}
    PREFIX ptex
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    INSTALL_COMMAND ""
    BUILD_IN_SOURCE 1
    BUILD_COMMAND cd src && make INSTALLDIR=${CMAKE_INSTALL_PREFIX} && cd ..
)

