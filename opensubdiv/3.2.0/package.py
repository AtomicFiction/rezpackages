
name = 'opensubdiv'

version = '3.2.0'

build_requires = [
    'glfw-3'
]

requires = [
    'tbb-4'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7']
]

tools = [
    'far_perf'
    'far_regression'
    'hbr_baseline'
    'hbr_regression'
    'stringify'
    'tutorials'
]

uuid = 'opensubdiv'

def commands():

    env.PATH.append('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib')

    if building:
        env.CPATH.append('{root}/include')
        env.LIBRARY_PATH.append('{root}/lib')

