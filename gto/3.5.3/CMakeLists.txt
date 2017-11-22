CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(gto_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_gto gto/open-gto-${gto_version}.tar.gz
    https://open-gto.googlecode.com/files/open-gto-${gto_version}.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()


if(APPLE)    
    set(config_options "")
else(UNIX)    
    set(config_options --enable-static --with-pic)            
endif()

ExternalProject_add(
    gto_build
    URL ${url_gto}
    PREFIX gto
    CONFIGURE_COMMAND ./bootstrap && ./configure --prefix=${CMAKE_INSTALL_PREFIX} ${config_options}
    INSTALL_COMMAND ${install_cmd}
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make
)

ExternalProject_Get_Property(gto_build source_dir)
set(PYTHON_SRC_DIR ${source_dir}/plugins/python)

install(
    CODE
    "execute_process(
        WORKING_DIRECTORY ${PYTHON_SRC_DIR}
        COMMAND python ./setup.py install --prefix=${CMAKE_INSTALL_PREFIX}/python        
    )"
)
