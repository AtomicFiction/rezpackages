name = 'sip'

version = '4.19.6'

authors = [
    'Riverbank Computing Limited <https://www.riverbankcomputing.com>'
]

description = \
    '''
    SIP is a tool that makes it very easy to create Python bindings for C and
    C++ libraries.
    '''

build_requires = [
    'python-2.7',
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7']
]

uuid = 'sip'

def commands():
    env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/lib64/site-packages')

    if building:
        env.CPATH.append('{root}/include')


