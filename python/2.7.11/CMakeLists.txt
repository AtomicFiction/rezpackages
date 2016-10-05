CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(python_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_python python/Python-${python_version}.tgz
    https://www.python.org/ftp/python/${python_version}/Python-${python_version}.tgz
)

#set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)
set(make_args VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

SET(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/lib")

if(APPLE)
    set(config_options --enable-shared)
elseif(UNIX)
    set(config_options --enable-ipv6 --enable-unicode=ucs2 --enable-shared --with-system-ffi --with-system-expat LDFLAGS=-Wl,-rpath=${CMAKE_INSTALL_PREFIX}/lib)
endif()

set(configure_cmd ./configure --prefix=${CMAKE_INSTALL_PREFIX} ${config_options})

ExternalProject_add(
    python
    URL ${url_python}
    PREFIX python
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND "${configure_cmd}"
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make ${make_args}
)
