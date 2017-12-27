name = 'maya'

version = '2016.5'

description = 'Maya'

build_requires = []

variants = [
    ['platform-linux']
]

uuid = 'maya'


def commands():
    env.MAYA_VERSION = '2016.5'
    env.MAYA_LOCATION = '/usr/autodesk/maya/maya${MAYA_VERSION}'
    env.PATH.prepend('${MAYA_LOCATION}')

    if building:
        env.MAYA_INCLUDE = ('${MAYA_LOCATION}/include')