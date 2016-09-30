name = "virtualenv"

version = "15.0.3"

build_requires = [
    "python-2.7",
    "pip"
]

variants = [
    ["platform-linux", 'arch-x86_64', "python-2.7"]
]

requires = [
	"python-2.7"
]

def commands():
    env.PYTHONPATH.append("{root}/python")
    env.PATH.append("{root}/bin")

uuid = "repository.virtualenv"    