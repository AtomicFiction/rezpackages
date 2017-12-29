name = 'houdini'

version = '16.0.633'

description = 'Houdini'

variants = [
    ['platform-linux']
]

uuid = 'houdini'

def commands():
    env.HOUDINI_TEMP_DIR = '/var/cache/houdini'
    env.HOUDINI_BUILD_VERSION = '633'
    env.HOUDINI_LOCATION = '/opt/sidefx/houdini/houdini{version}'
    env.HOUDINI_MINOR_RELEASE = '0'
    env.HOUDINI_VERSION = '{version}'
    env.HOUDINI_BASE_VERSION = '16.0'
    env.HOUDINI_PATH_VERSIONS = '15.5'
    env.HOUDINI_MAJOR_RELEASE = '16'
    env.HOUDINI_PATH = '/var/tmp/houdini16.0:&'

