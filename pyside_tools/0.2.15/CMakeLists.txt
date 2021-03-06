CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(pyside_tools_version $ENV{REZ_BUILD_PROJECT_VERSION})

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    pyside_tools
    GIT_REPOSITORY git@github.com:AtomicFiction/Tools.git
    GIT_TAG ${pyside_tools_version}
    PREFIX pyside_tools
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
               -DBUILD_TESTS=FALSE
               -DCMAKE_PREFIX_PATH=$ENV{REZ_PYSIDE_ROOT}
               -DCMAKE_SKIP_BUILD_RPATH=FALSE
               -DCMAKE_BUILD_WITH_INSTALL_RPATH=FALSE 
               -DCMAKE_INSTALL_RPATH=$ENV{REZ_QT_ROOT}/lib:${CMAKE_INSTALL_PREFIX}/lib
)
