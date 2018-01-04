CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(pyqt_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_pyqt pyqt/PyQt4_gpl_x11-${pyqt_version}.tar.gz
    http://tcpdiag.dl.sourceforge.net/project/pyqt/PyQt4/PyQt-${pyqt_version}/PyQt4_gpl_x11-${pyqt_version}.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT})

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    pyqt_build
    URL ${url_pyqt}
    PREFIX pyqt
    CONFIGURE_COMMAND python ./configure-ng.py --confirm-license --sysroot=${CMAKE_INSTALL_PREFIX} --sip=$ENV{REZ_SIP_ROOT}/bin/sip --sip-incdir=$ENV{REZ_SIP_ROOT}/include/python2.7
    INSTALL_COMMAND ${install_cmd}
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make ${make_args}
)
