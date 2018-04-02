CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(RezPipInstall)

set(package_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    package_url python_libraries/numpy-${package_version}.zip
    ""
)

set(pipargs --ignore-installed --verbose)

rez_pip_install(
    numpy
    URL ${package_url}
    PIPARGS ${pipargs}
)

install(CODE "message(STATUS Running Phony install)")
