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

ExternalProject_add(
    qt
    URL ${url_qt}
    PREFIX qt
    UPDATE_COMMAND ""
    #CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} -confirm-license -opensource -no-webkit -no-openvg -system-sqlite -openssl-linked -dbus-linked -release -nomake example -optimized-qmake
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} -confirm-license -opensource -system-sqlite -openssl-linked -dbus-linked -release -nomake example -nomake demos -optimized-qmake
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make ${make_args}
)
