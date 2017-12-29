name = 'prman'

version = '21.0'

description = 'Pixar RenderMan'

build_requires = []

variants = [
    ['platform-linux']
]

uuid = 'prman'

def commands():
    env.PRMAN_VERSION = '21.0'
    env.PRMAN_LOCATION = '/opt/pixar/RenderManProServer-${PRMAN_VERSION}'
    env.RMANTREE = '${PRMAN_LOCATION}'
    env.PATH.prepend('${RMANTREE}/bin')