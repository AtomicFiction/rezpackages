CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(scons_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_scons scons/scons-${scons_version}.tar.gz
    http://downloads.sourceforge.net/scons/scons-${scons_version}.tar.gz
)

if(${REZ_BUILD_INSTALL})
    set(install_cmd python ./setup.py install --prefix=${CMAKE_INSTALL_PREFIX} --standard-lib --optimize=1 --install-data=${CMAKE_INSTALL_PREFIX}/share)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    scons
    URL ${url_scons}
    PREFIX scons
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    INSTALL_COMMAND ${install_cmd}
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ""
)
