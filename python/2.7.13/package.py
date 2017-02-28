name = 'python'

version = '2.7.13'

tools = ['python']

variants = [
    ['platform-linux', 'arch-x86_64', 'os-Fedora-25']
]

def commands():
    env.PATH.append('/usr/bin')
