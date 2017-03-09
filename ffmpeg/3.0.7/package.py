name = "ffmpeg"

version = "3.0.7"

authors = [
    "FFMPEG"
]

description = \
    """
    FFMPEG.
    """

build_requires = [
    "gcc-4.8.2+"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

uuid = "repository.ffmpeg"

def commands():
    env.PATH.append('{root}/bin')
    if building:
        env.FFMPEG_INCLUDE_DIR = "{root}/include"

        # static libs only, hence build-time only
        env.LD_LIBRARY_PATH.append("{root}/lib")
