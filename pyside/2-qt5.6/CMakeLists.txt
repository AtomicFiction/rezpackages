CMAKE_MINIMUM_REQUIRED(VERSION 3.1)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(pyside_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_pyside pyside/pyside-${pyside_version}.tar.gz
    "" # Package had to be built manually
)

if(${REZ_BUILD_INSTALL})
    set(install_cmd python setup.py install --prefix=${CMAKE_INSTALL_PREFIX} --skip-build --jobs=$ENV{REZ_BUILD_THREAD_COUNT})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    pyside
    URL ${url_pyside}
    PREFIX pyside
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_COMMAND python setup.py build --no-examples --ignore-git --jobs=$ENV{REZ_BUILD_THREAD_COUNT}
    INSTALL_COMMAND ${install_cmd}
    BUILD_IN_SOURCE 1
)

