CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezPipInstall)

set(package_version $ENV{REZ_BUILD_PROJECT_VERSION})
set(package_name $ENV{REZ_BUILD_PROJECT_NAME})

set(url "$ENV{REZ_REPO_PAYLOAD_DIR}/python-libraries/${package_name}-${package_version}.tar.gz")

rez_pip_install(
    virtualenv
    URL ${url}
)
