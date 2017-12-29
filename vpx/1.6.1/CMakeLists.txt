CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(vpx_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_vpx vpx/libvpx-${vpx_version}.tar.bz2
    http://storage.googleapis.com/downloads.webmproject.org/releases/webm/libvpx-${vpx_version}.tar.bz2
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    vpx
    URL ${url_vpx}
    PREFIX vpx
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --disable-examples --disable-unit-tests --enable-vp9-highbitdepth --as=yasm --enable-pic
    INSTALL_COMMAND "${install_cmd}"
    BUILD_COMMAND make ${make_args}
    BUILD_IN_SOURCE 1
)

