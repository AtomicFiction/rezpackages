name = "katana"

version = "2.5.4"

description = "Katana"

build_requires = []

variants = [
    ["platform-linux"]
]

uuid = "katana"


def commands():
    env.KATANA_VERSION = "2.5v4"
    env.KATANA_LOCATION = "/opt/thefoundry/katana/katana${KATANA_VERSION}"
    env.PATH.prepend("${KATANA_LOCATION}")
    env.KATANA_RESOURCES=''

    if building:
        env.KATANA_INCLUDE = "${KATANA_LOCATION}/plugin_apis/include"
        env.CPATH.append("${KATANA_LOCATION}/plugin_apis/include")
