name = 'python'

version = '2.7.10'

tools = ['python']

variants = [    
    ['platform-linux', 'arch-x86_64', 'os-CentOS-6.5']
]

def commands():
    env.PATH.append('/home/cmartin/opt/python/python2.7.10/bin')
    env.LD_LIBRARY_PATH.append('/home/cmartin/opt/python/python2.7.10/lib')
