name = 'python'

version = '2.7.10'

tools = ['python']

variants = [
    ['platform-linux'],
    ['platform-linux', 'arch-x86_64', 'os-CentOS-6.5']
]

def commands():
    env.PATH.append('/usr/local/python2.7.10/bin/')
