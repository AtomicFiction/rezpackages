CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(version $ENV{REZ_BUILD_PROJECT_VERSION})

if(NOT ${REZ_BUILD_INSTALL})
    message(FATAL_ERROR "Must install this package with -i flag")
endif()

rez_set_archive(
    url pip/pip-${version}.tar.gz
    https://github.com/pypa/pip/archive/${version}.tar.gz
)

set(PYTHON_VERSION "$ENV{REZ_PYTHON_MAJOR_VERSION}.$ENV{REZ_PYTHON_MINOR_VERSION}")
set(PIP_PYTHONPATH ${CMAKE_INSTALL_PREFIX}/lib/python${PYTHON_VERSION}/site-packages)

if(${REZ_BUILD_INSTALL})
    set(install_cmd export PYTHONPATH=$PYTHONPATH:${PIP_PYTHONPATH} && python setup.py install --prefix=${CMAKE_INSTALL_PREFIX} --skip-build)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    pip
    URL ${url}
    PREFIX pip
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_IN_SOURCE 1
    BUILD_COMMAND python setup.py build
    INSTALL_COMMAND ${install_cmd}
)
