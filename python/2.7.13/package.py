name = 'python'

version = '2.7.13'

tools = ['python']

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7']
]

def commands():
    env.PATH.append('/usr/bin')
