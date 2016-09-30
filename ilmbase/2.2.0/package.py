name = 'ilmbase'

version = '2.2.0'

authors = [
    'ILM'
]

description = \
    '''
    Utility libraries from ILM used by OpenEXR.
    '''

build_requires = [    
]

variants = [
    ['platform-linux', 'arch-x86_64']
]

uuid = 'repository.ilmbase'

def commands():
    if building:
        env.ILMBASE_HOME = '{root}'
        env.ILMBASE_VERSION = '2.2.0'
        env.ILMBASE_INCLUDE_DIR = '{root}/include'

        # static libs only, hence build-time only
        env.LD_LIBRARY_PATH.append('{root}/lib')
