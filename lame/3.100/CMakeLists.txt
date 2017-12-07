CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(lame_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_lame lame/lame-${lame_version}.tar.gz
    https://sourceforge.net/projects/lame/files/lame/${lame_version}/lame-${lame_version}.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    lame
    URL ${url_lame}
    PREFIX lame
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --disable-shared --enable-nasm --with-pic
    INSTALL_COMMAND "${install_cmd}"
    BUILD_COMMAND make ${make_args}
    BUILD_IN_SOURCE 1
)

