CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(tbb_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_tbb tbb/tbb-${tbb_version}.tar.gz
    https://github.com/01org/tbb/archive/${tbb_version}.tar.gz
)

set(build_prefix "tbb_build")

ExternalProject_add(
    tbb
    URL ${url_tbb}
    PREFIX tbb
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    INSTALL_COMMAND ""
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make tbb_build_prefix="${build_prefix}" -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1
)

ExternalProject_Get_Property(tbb SOURCE_DIR)

set(include_dir ${SOURCE_DIR}/include)
set(release_dir ${SOURCE_DIR}/build/${build_prefix}_release)

install(DIRECTORY ${include_dir}/ DESTINATION ${CMAKE_INSTALL_PREFIX}/include
        FILES_MATCHING PATTERN "*.h")

install(DIRECTORY ${release_dir}/ DESTINATION ${CMAKE_INSTALL_PREFIX}/lib/release
        FILES_MATCHING PATTERN "*.so*")

