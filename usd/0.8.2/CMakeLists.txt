CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(usd_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_usd usd/USD-${usd_version}.tar.gz
    https://github.com/PixarAnimationStudios/USD/archive/v${usd_version}.tar.gz
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

               -DPXR_BUILD_TESTS=OFF

               -DTBB_ROOT_DIR=$ENV{REZ_TBB_ROOT}
               -DTBB_LIBRARY=$ENV{REZ_TBB_ROOT}/lib/release

               -DBOOST_ROOT=$ENV{REZ_BOOST_ROOT}
               -DBoost_NO_SYSTEM_PATHS=ON

               -DOPENEXR_INCLUDE_DIR=$ENV{REZ_ILMBASE_ROOT}/include
               -DOPENEXR_LIBRARY_DIR=$ENV{REZ_OPENEXR_ROOT}/lib
               -DOPENEXR_Half_LIBRARY=$ENV{REZ_ILMBASE_ROOT}/lib/libHalf.a
               -DOPENEXR_Iex_LIBRARY=$ENV{REZ_ILMBASE_ROOT}/lib/libIex.a

               -DOPENSUBDIV_ROOT_DIR=$ENV{REZ_OPENSUBDIV_ROOT}
               -DOIIO_LOCATION=$ENV{REZ_OPENIMAGEIO_ROOT}
               -DPTEX_LOCATION=$ENV{REZ_PTEX_ROOT}

               -DPXR_BUILD_ALEMBIC_PLUGIN=ON
               -DALEMBIC_DIR=$ENV{REZ_ALEMBIC_ROOT}

               -DPXR_BUILD_MAYA_PLUGIN=ON
               -DPXR_MAYA_TBB_BUG_WORKAROUND=ON
               -DMAYA_LOCATION=$ENV{MAYA_LOCATION}

               -DPXR_BUILD_KATANA_PLUGIN=ON

               -DPXR_BUILD_HOUDINI_PLUGIN=ON
               -DHOUDINI_ROOT=$ENV{HOUDINI_LOCATION}

               -DCMAKE_SKIP_BUILD_RPATH=FALSE
               -DCMAKE_BUILD_WITH_INSTALL_RPATH=FALSE
               -DCMAKE_INSTALL_RPATH=$ENV{REZ_BOOST_ROOT}/lib:$ENV{REZ_TBB_ROOT}/lib/release:$ENV{REZ_OPENSUBDIV_ROOT}/lib:$ENV{REZ_PTEX_ROOT}/lib:${CMAKE_INSTALL_PREFIX}/lib
)

