name = "pyqt"

version = "4.10.1"

build_requires = [
    "qt-4.8",
    "python-2.7",
    "sip-4.16"
]

requires = [
    "qt-4.8",
    "sip-4.16",
    "python-2.7"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

uuid = "pyqt"

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append('{root}/python')

    if building:
        env.GTO_INCLUDE_DIR = "{root}/include"

