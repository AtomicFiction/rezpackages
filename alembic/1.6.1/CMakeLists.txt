CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(alembic_version $ENV{REZ_BUILD_PROJECT_VERSION})

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    alembic
    GIT_REPOSITORY git@github.com:AtomicFiction/alembic.git
    GIT_TAG 1.6.1
    PREFIX alembic
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
        -DUSE_PYALEMBIC=ON
        -DBOOST_ROOT=$ENV{REZ_BOOST_ROOT}
        -DPYILMBASE_ROOT=$ENV{REZ_PYILMBASE_ROOT}
        -DILMBASE_ROOT=$ENV{REZ_ILMBASE_ROOT}
        -DUSE_HDF5=ON
        -DUSE_TESTS=OFF
        -DUSE_STATIC_BOOST=ON
        -DALEMBIC_LIB_USES_BOOST=ON
        -DUSE_STATIC_HDF5=ON
        -DALEMBIC_ILMBASE_LINK_STATIC=ON
        -DUSE_MAYA=ON
        -DCMAKE_CXX_FLAGS=-ldl
        -DCMAKE_SKIP_BUILD_RPATH=FALSE
        -DCMAKE_BUILD_WITH_INSTALL_RPATH=FALSE
        -DCMAKE_INSTALL_RPATH=$ENV{REZ_HDF5_ROOT}/lib:$ENV{REZ_ILMBASE_ROOT}/lib:$ENV{REZ_OPENEXR_ROOT}/lib:$ENV{REZ_PYILMBASE_ROOT}/lib:${CMAKE_INSTALL_PREFIX}/lib
)
