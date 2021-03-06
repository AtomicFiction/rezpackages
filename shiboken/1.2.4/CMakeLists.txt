CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(shiboken_version $ENV{REZ_BUILD_PROJECT_VERSION})

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    shiboken
    GIT_REPOSITORY git@github.com:AtomicFiction/Shiboken.git
    GIT_TAG ${shiboken_version}
    PREFIX shiboken
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
               -DBUILD_TESTS=False
               -DCMAKE_INSTALL_RPATH=${CMAKE_INSTALL_PREFIX}/lib
)
