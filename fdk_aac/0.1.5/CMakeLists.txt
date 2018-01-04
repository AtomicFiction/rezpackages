CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(fdk-aac_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_fdk-aac fdk-aac/fdk-aac-${fdk-aac_version}.tar.gz
    https://github.com/mstorsjo/fdk-aac/archive/v${fdk-aac_version}.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    fdk-aac
    URL ${url_fdk-aac}
    PREFIX fdk-aac
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND autoreconf -fiv && ./configure --prefix=${CMAKE_INSTALL_PREFIX} --disable-shared --with-pic
    INSTALL_COMMAND "${install_cmd}"
    BUILD_COMMAND make ${make_args}
    BUILD_IN_SOURCE 1
)

