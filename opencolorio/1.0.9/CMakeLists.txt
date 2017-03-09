CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(opencolorio_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_opencolorio opencolorio/opencolorio-${opencolorio_version}.tar.gz
    http://download.savannah.nongnu.org/releases/openexr/openexr-${openexr_version}.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    opencolorio
    PREFIX opencolorio
    #GIT_REPOSITORY https://github.com/imageworks/OpenColorIO.git
    #GIT_TAG v${opencolorio_version}
    URL ${url_opencolorio}
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DCMAKE_SKIP_BUILD_RPATH=OFF
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=OFF
    -DCMAKE_INSTALL_RPATH=${CMAKE_INSTALL_PREFIX}/lib
)
