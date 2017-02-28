CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

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

ExternalProject_add(
    openimageio
    GIT_REPOSITORY https://github.com/OpenImageIO/oiio.git
    GIT_TAG Release-${openimageio_version}
    PREFIX openimageio
    CMAKE_ARGS 
    -DUSE_PYTHON=ON
    -DBOOST_ROOT=$ENV{REZ_BOOST_ROOT}
    -DBOOST_LIBRARYDIR=$ENV{REZ_BOOST_ROOT}/lib
    -DILMBASE_HOME=$ENV{REZ_ILMBASE_ROOT}
    -DOPENEXR_HOME=$ENV{REZ_OPENEXR_ROOT}
    -DOPENEXR_INCLUDE_DIR=$ENV{OPENEXR_INCLUDE_DIR}
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
)