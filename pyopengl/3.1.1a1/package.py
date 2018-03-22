name = 'pyopengl'

version = '3.1.1a1'

authors = [
    'Mike C. Fletcher <mcfletch@vrplumber.com>'
]

description = \
    '''
    Standard OpenGL bindings for Python.
    '''

build_requires = [
    'setuptools'
]

requires = [
    'python'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7']
]

uuid = 'pyopengl'

def commands():
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')

