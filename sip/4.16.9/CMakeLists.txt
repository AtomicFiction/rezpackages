CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(package_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url sip/sip-${package_version}.tar.gz
    http://iweb.dl.sourceforge.net/project/pyqt/sip/sip-${package_version}/sip-${package_version}.tar.gz
)

set(make_args VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()

set(bind_dir ${CMAKE_INSTALL_PREFIX}/bin)
set(inc_dir ${CMAKE_INSTALL_PREFIX}/include)
set(mod_dir ${CMAKE_INSTALL_PREFIX}/python)

ExternalProject_add(
    package_build
    URL ${url}
    PREFIX sip
    CONFIGURE_COMMAND python ./configure.py --bindir=${bind_dir} --destdir=${mod_dir} --incdir=${inc_dir}
    INSTALL_COMMAND ${install_cmd}
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make
)