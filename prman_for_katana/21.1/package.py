name = "prman_for_katana"

version = "21.1"

description = "Pixar RenderMan For Katana"

requires = [
    'prman-21',
    'katana-2.5'
]

build_requires = []

variants = [
    ["platform-linux"]
]

uuid = "prman_for_katana"


def commands():
    env.RFKTREE = '/opt/pixar/RenderManForKatana-21.1-katana2.5'
    env.KATANA_RESOURCES.append('${RFKTREE}/plugins/Resources/PRMan21')
