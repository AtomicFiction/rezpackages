CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(openvdb_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_openvdb openvdb/openvdb-${openvdb_version}.tar.gz
    http://www.openvdb.org/download/openvdb_5_1_0_library.zip
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1 LOG4CPLUS_LIB= )

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    openvdb
    URL ${url_openvdb}
    PREFIX openvdb
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make ${make_args}
)


