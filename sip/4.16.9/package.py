name = "sip"

version = "4.16.9"

build_requires = [
    "python-2.7"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

uuid = "sip"

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append('{root}/python')

    if building:
        env.SIP_INCLUDE_DIR = "{root}/include"


