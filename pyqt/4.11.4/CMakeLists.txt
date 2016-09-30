CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(package_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url pyqt/PyQt-x11-gpl-${package_version}.tar.gz
    http://tcpdiag.dl.sourceforge.net/project/pyqt/PyQt4/PyQt-${package_version}/PyQt-x11-gpl-${package_version}.tar.gz
)

set(make_args VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()

set(bin_dir ${CMAKE_INSTALL_PREFIX}/bin)
set(inc_dir ${CMAKE_INSTALL_PREFIX}/include)
set(mod_dir ${CMAKE_INSTALL_PREFIX}/python)
set(sip_dir ${CMAKE_INSTALL_PREFIX}/sip)

ExternalProject_add(
    package_build
    URL ${url}
    PREFIX pyqt
    CONFIGURE_COMMAND python ./configure.py --confirm-license --bindir=${bin_dir} --destdir=${mod_dir} --sipdir=${sip_dir}
    INSTALL_COMMAND ${install_cmd}
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make
)