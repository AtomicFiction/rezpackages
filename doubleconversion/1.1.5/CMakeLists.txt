CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(doubleconversion_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_doubleconversion doubleconversion/double-conversion-${doubleconversion_version}.tar.gz
    https://github.com/google/double-conversion/archive/v${doubleconversion_vesrion}.tar.gz
)

if(${REZ_BUILD_INSTALL})
    set(install_cmd scons DESTDIR=${CMAKE_INSTALL_PREFIX} install)
else()
    set(install_cmd "")
endif()

# Static
ExternalProject_add(
    doubleconversion
    URL ${url_doubleconversion}
    PREFIX doubleconversion
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
)

# Shared
ExternalProject_add(
    doubleconversion_shared
    URL ${url_doubleconversion}
    PREFIX doubleconversion_shared
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DBUILD_SHARED_LIBS=ON
)
