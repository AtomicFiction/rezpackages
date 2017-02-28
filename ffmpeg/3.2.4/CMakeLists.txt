CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(ffmpeg_version $ENV{REZ_BUILD_PROJECT_VERSION})

#if(${REZ_BUILD_INSTALL})
#    set(install_cmd make install ${make_args})
#else()
#    set(install_cmd "")
#endif()

add_custom_target(
    build_ffmpeg
    ALL
    COMMAND bash ./build.sh ${CMAKE_BINARY_DIR} ${CMAKE_INSTALL_PREFIX} $ENV{REZ_REPO_PAYLOAD_DIR} ${ffmpeg_version}
    WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}
    VERBATIM
)