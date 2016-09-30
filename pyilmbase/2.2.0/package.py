name = 'pyilmbase'

version = '2.2.0'

authors = [
    'ILM'
]

description = \
    '''
    Python Bindings for Utility libraries from ILM used by OpenEXR.
    '''

build_requires = [    
    'python-2.7',
    'ilmbase-2.2.0',
    'boost-1.55.0'
]

requires = [
    'python-2.7'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'python-2.7']
]

uuid = 'repository.pyilmbase-2.2.0'

def commands():
    env.PYTHONPATH.append('{root}/lib64/python2.7/site-packages')
    env.LD_LIBRARY_PATH.append('{root}/lib')

    if building:
        env.PYILMBASE_HOME = '{root}'
        env.PYILMBASE_INCLUDE_DIR = '{root}/include'
