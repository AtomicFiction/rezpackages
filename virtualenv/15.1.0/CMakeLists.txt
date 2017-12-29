CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_virtualenv virtualenv/virtualenv-${version}.tar.gz
    https://github.com/pypa/virtualenv/archive/${version}.tar.gz
)

set(PYTHON_VERSION "$ENV{REZ_PYTHON_MAJOR_VERSION}.$ENV{REZ_PYTHON_MINOR_VERSION}")
set(VIRTUALENV_PYTHONPATH ${CMAKE_INSTALL_PREFIX}/lib/python${PYTHON_VERSION}/site-packages)

if(${REZ_BUILD_INSTALL})
    set(install_cmd export PYTHONPATH=$PYTHONPATH:${VIRTUALENV_PYTHONPATH} && python ./setup.py install --prefix=${CMAKE_INSTALL_PREFIX} --skip-build)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    virtualenv
    URL ${url_virtualenv}
    PREFIX virtualenv
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_IN_SOURCE 1
    BUILD_COMMAND python setup.py build
    INSTALL_COMMAND ${install_cmd}
)
