CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(shiboken_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_shiboken shiboken/Shiboken-${shiboken_version}.tar.gz
    https://codeload.github.com/PySide/Shiboken/tar.gz/1.2.4/Shiboken-${shiboken_version}.tar.gz    
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

FIND_PACKAGE(PythonInterp REQUIRED)

ExternalProject_add(
    shiboken
    URL ${url_shiboken}
    PREFIX shiboken        
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
               #-DPYTHON_LIBRARY=$ENV{REZ_PYTHON_ROOT}/python/lib/libpython2.7.so
               -DBUILD_TESTS=False
               -DCMAKE_BUILD_TYPE=Release 
)