CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(alembic_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_alembic alembic/alembic-${alembic_version}.tar.gz
    http://download.savannah.nongnu.org/releases/alembic/alembic-${alembic_version}.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    alembic
    URL ${url_alembic}
    PREFIX alembic
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DUSE_PYALEMBIC=ON
    -DBOOST_ROOT=${REZ_BOOST_ROOT}
    -DPYILMBASE_ROOT=$ENV{REZ_PYILMBASE_ROOT}
    -DILMBASE_ROOT=$ENV{REZ_ILMBASE_ROOT}
    -DBoost_INCLUDE_DIR=$ENV{BOOST_INCLUDE_DIR}
    -DUSE_HDF5=ON
    -DUSE_STATIC_BOOST=ON
    -DUSE_STATIC_HDF5=ON
    -DALEMBIC_ILMBASE_LINK_STATIC=ON
    -DCMAKE_MODULE_LINKER_FLAGS="-ldl"
    -DCMAKE_SHARED_LINKER_FLAGS="-ldl"
)
