CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(imagemagick_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_imagemagick imagemagick/ImageMagick-${imagemagick_version}.tar.gz
    https://codeload.github.com/ImageMagick/ImageMagick/tar.gz/${imagemagick_version}
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT})

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    imagemagick
    URL ${url_imagemagick}
    PREFIX imagemagick
    BUILD_IN_SOURCE 1
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX}
    BUILD_COMMAND make ${make_args}
    INSTALL_COMMAND "${install_cmd}"
)

