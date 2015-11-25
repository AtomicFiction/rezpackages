CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(package_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url qt/qt-everywhere-opensource-src-${package_version}.tar.gz
    https://open-gto.googlecode.com/files/open-gto-${package_version}.tar.gz
)

set(make_args VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    package_build
    URL ${url}
    PREFIX qt
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} -openssl -release -opensource -confirm-license -no-webkit
    INSTALL_COMMAND ${install_cmd}
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make
)

ExternalProject_Get_Property(package_build source_dir)
set(PYTHON_SRC_DIR ${source_dir}/plugins/python)


# mv ${WORK_DIR}/extract/qt-everywhere-opensource-src-${package_version}/build/* ${CMAKE_INSTALL_PREFIX}
# printf "[Paths]\nPrefix = /opt/${PRODUCT}/${PRODUCT}-${PRODUCT_VERSION}\n" > ${CMAKE_INSTALL_PREFIX}/bin/qt.conf

# install(
#     CODE
#     "execute_process(
#         WORKING_DIRECTORY ${PYTHON_SRC_DIR}
#         COMMAND python ./setup.py install --prefix=${CMAKE_INSTALL_PREFIX}/python        
#     )"
# )