name = 'python'

version = '2.7.11'

tools = ['python']

variants = [    
    ['platform-linux', 'arch-x86_64', 'os-CentOS-6']
]

def commands():
    env.PATH.append('/home/cmartin/opt/python/python2.7.11/bin')    
