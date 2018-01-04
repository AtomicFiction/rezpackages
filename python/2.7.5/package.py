name = 'python'

version = '2.7.5'

tools = ['python']

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7']
]

def commands():
    env.PATH.append('/usr/bin')
    env.PYTHONPATH.append('/usr/lib64/python2.7/site-packages')
    env.LD_LIBRARY_PATH.append('/usr/lib64')

    if building:
        env.CPATH.append('/usr/include/python2.7')
        env.PKG_CONFIG_PATH.append('/usr/lib64/pkgconfig')

