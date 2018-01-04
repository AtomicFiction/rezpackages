CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(opensubdiv_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_opensubdiv opensubdiv/opensubdiv-${opensubdiv_version}.tar.gz
    https://github.com/PixarAnimationStudios/OpenSubdiv/archive/v${opensubdiv_version}.tar.gz    
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    opensubdiv
    URL ${url_opensubdiv}
    PREFIX opensubdiv
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} 
               -DNO_PTEX=ON
               -DNO_DOC=ON
               -DNO_CUDA=ON
               -DNO_OPENCL=ON
               -DNO_CLEW=ON
               -DCMAKE_SKIP_BUILD_RPATH=FALSE
               -DCMAKE_BUILD_WITH_INSTALL_RPATH=FALSE
               -DCMAKE_INSTALL_RPATH=$ENV{REZ_TBB_ROOT}/lib/release:${CMAKE_INSTALL_PREFIX}/lib
)

