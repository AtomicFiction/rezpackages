CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(x265_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_x265 x265/x265_${x265_version}.tar.gz
    https://bitbucket.org/multicoreware/x265/downloads/x265_${x265_version}.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    x265
    URL ${url_x265}
    PREFIX x265
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ${CMAKE_COMMAND} -G "Unix Makefiles" source
               -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
               -DENABLE_SHARED=OFF
               -DPOSITION_INDEPENDENT_CODE=ON
    BUILD_COMMAND make ${make_args}
    INSTALL_COMMAND ${install_cmd}
    BUILD_IN_SOURCE 1
)

