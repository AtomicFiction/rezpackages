CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(usd_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_usd usd/USD-${usd_version}.tar.gz
    https://github.com/PixarAnimationStudios/OpenSubdiv/archive/v${usd_version}.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    usd
    URL ${url_usd}
    PREFIX usd
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
               -DTBB_tbb_LIBRARY=$ENV{REZ_TBB_ROOT}/lib/release/libtbb.so
               -DTBB_INCLUDE_DIRS=$ENV{REZ_TBB_ROOT}/include
               -DOPENEXR_LOCATION=$ENV{REZ_OPENEXR_ROOT}
               -DOPENEXR_INCLUDE_DIR=$ENV{REZ_ILMBASE_ROOT}/include
               -DOPENEXR_LIBRARY_DIR=$ENV{REZ_OPENEXR_ROOT}/lib
               -DOPENEXR_Half_LIBRARY=$ENV{REZ_ILMBASE_ROOT}/lib/libHalf.a
               -DOIIO_BASE_DIR=$ENV{REZ_OPENIMAGEIO_ROOT}
               -DPTEX_INCLUDE_DIR=$ENV{PTEX_INCLUDE_DIR}
               -DOPENSUBDIV_INCLUDE_DIR=$ENV{REZ_OPENSUBDIV_ROOT}/include
               -OPENSUBDIV_ROOT_DIR=$ENV{REZ_OPENSUBDIV_ROOT}
               -DBOOST_ROOT=$ENV{REZ_BOOST_ROOT}
               -DPYSIDE_BIN_DIR=$ENV{REZ_PYSIDE_ROOT}/bin
               -DPXR_BUILD_MAYA_PLUGIN=TRUE
               -DMAYA_LOCATION=/opt/autodesk/maya/maya2016EXT2-x64
               -DMAYA_tbb_LIBRARY=$ENV{REZ_TBB_ROOT}/lib/release/libtbb.so
               -DPXR_MAYA_TBB_BUG_WORKAROUND=ON
               -DPXR_BUILD_KATANA_PLUGIN=TRUE
               -DKATANA_API_LOCATION=/opt/thefoundry/katana/katana2.5v4
               -DPXR_ENABLE_NAMESPACES=ON
)

