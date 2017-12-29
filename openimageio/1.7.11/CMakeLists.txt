CMAKE_MINIMUM_REQUIRED(VERSION 2.8.11)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(openimageio_version $ENV{REZ_BUILD_PROJECT_VERSION})

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

include(FindPkgConfig)

pkg_check_modules(FFMPEG REQUIRED 
    libavcodec
    libavdevice
    libavfilter
    libavformat
    libavutil
    libpostproc
    libswresample
    libswscale
)

string(REPLACE ";" "|"  FFMPEG_LIBRARIES_BAR_SEP "${FFMPEG_LIBRARIES}")

ExternalProject_add(
    openimageio
    GIT_REPOSITORY https://github.com/OpenImageIO/oiio.git
    GIT_TAG Release-${openimageio_version}
    PREFIX openimageio
    LIST_SEPARATOR |
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
               -DLINKSTATIC=ON
               -DBUILDSTATIC=ON
               -DUSE_PYTHON=ON
               -DUSE_fPIC=ON
               -DOIIO_BUILD_TESTS=OFF
               -DBOOST_ROOT=$ENV{REZ_BOOST_ROOT}
               -DILMBASE_HOME=$ENV{REZ_ILMBASE_ROOT}
               -DOPENEXR_HOME=$ENV{REZ_OPENEXR_ROOT}
               -DFFMPEG_INCLUDE_DIR=${FFMPEG_INCLUDE_DIRS}
               -DFFMPEG_LIBRARIES=${FFMPEG_LIBRARIES_BAR_SEP}
               -DCMAKE_SKIP_BUILD_RPATH=FALSE
               -DCMAKE_BUILD_WITH_INSTALL_RPATH=FALSE
               -DCMAKE_INSTALL_RPATH=$ENV{REZ_QT_ROOT}/lib:${CMAKE_INSTALL_PREFIX}/lib
)
