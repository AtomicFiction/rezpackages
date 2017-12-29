name = 'python'

version = '2.7.11'

build_requires = [
]

variants = [
    ['platform-linux', 'arch-x86_64'],
    ['platform-osx', 'arch-x86_64']
]

def commands():
    env.PATH.append('{root}/bin')
    
    if building:        
        env.PYTHON_INCLUDE_DIR = '{root}/include'        


uuid = 'repository.python'        
