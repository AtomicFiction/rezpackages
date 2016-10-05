name = "sip"

version = "4.16.9"

build_requires = [    
    "python-2.7"
]

variants = [
    ["platform-linux", "arch-x86_64"]
]


def commands():
    env.PATH.append("{root}/bin")    
    env.PYTHONPATH.append('{root}/python')
    
    if building:
        env.SIP_INCLUDE_DIR = "{root}/include"

uuid = "repository.sip"        