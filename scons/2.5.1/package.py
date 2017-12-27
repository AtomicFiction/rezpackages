name = "scons"

version = "2.5.1"

authors = [
    'Chad Austin',
    'Dirk Baechle',
    'Charles Crain',
    'William Deegan',
    'Steve Leblanc',
    'Rob Managan',
    'Greg Noel',
    'Gary Oberbrunner',
    'Anthony Roach',
    'Greg Spencer',
    'Tom Tanner',
    'Anatoly Techtonik',
    'Christoph Wiedemann',
    'Russel Winder'
]

description = \
    '''
    This is SCons, a tool for building software (and other files).  SCons is
    implemented in Python, and its "configuration files" are actually Python
    scripts, allowing you to use the full power of a real scripting language
    to solve build problems.  You do not, however, need to know Python to
    use SCons effectively.
    '''

requires = [
    "python-2.7"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7", "python-2.7"]
]

uuid = "scons"

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
    env.MANPATH.append('{root}/share/man')
