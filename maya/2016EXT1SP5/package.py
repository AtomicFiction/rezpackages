name = "maya"

version = "2016EXT1SP5"

description = "Maya"

build_requires = []

variants = [
    ["platform-linux"]
]

uuid = "maya"

def commands():
    env.MAYA_VERSION = "2016EXT1SP5"
    env.MAYA_LOCATION = "/opt/autodesk/maya/maya${MAYA_VERSION}-x64"
    env.PATH.prepend("${MAYA_LOCATION}/bin")

    if building:
        env.MAYA_INCLUDE = ("${MAYA_LOCATION}/include")
