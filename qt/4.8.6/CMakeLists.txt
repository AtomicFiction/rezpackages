CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(qt_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_qt qt/qt-everywhere-opensource-src-${qt_version}.tar.gz
    http://download.qt.io/archive/qt/4.8/4.8.6/qt-everywhere-opensource-src-${qt_version}.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()


if(APPLE)
    set(config_args -confirm-license -opensource -nomake example -nomake demos -optimized-qmake -release -no-framework)
    set(patch_command patch -p1 -t -N < $ENV{REZ_REPO_PAYLOAD_DIR}/qt/el-capitan.patch) 
else(UNIX)
    set(config_args -confirm-license -opensource -nomake example -nomake demos -optimized-qmake -release)
    set(patch_command )
else()
    set(config_args "")
endif()

ExternalProject_add(
    qt
    URL ${url_qt}
    PREFIX qt    
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} ${config_args}
    PATCH_COMMAND ${patch_command}
    INSTALL_COMMAND ${AF_MAKE_INSTALL_COMMAND}
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make ${AF_EXTRA_MAKE_ARGS}
)
