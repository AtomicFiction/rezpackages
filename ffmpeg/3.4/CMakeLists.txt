CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(ffmpeg_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_ffmpeg ffmpeg/ffmpeg-${ffmpeg_version}.tar.gz
    https://www.ffmpeg.org/releases/ffmpeg-${ffmpeg_version}.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    ffmpeg
    URL ${url_ffmpeg}
    PREFIX ffmpeg
    BUILD_IN_SOURCE 1
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --enable-pic --pkg-config-flags=--static --extra-libs=-lpthread --extra-libs=-lm --enable-gpl --enable-nonfree --enable-libx264 --enable-libx265 --enable-libfdk-aac --enable-libmp3lame --enable-libopus --enable-libvorbis --enable-libfreetype
    BUILD_COMMAND make ${make_args}
    INSTALL_COMMAND "${install_cmd}"
)

