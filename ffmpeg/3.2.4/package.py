name = "ffmpeg"

version = "3.2.4"

authors = [
    "FFMPEG"
]

description = \
    """
    FFMPEG.
    """

build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

tools = [
    "ffmpeg",
    "ffmpeg-10bit",
    "ffserver",
    "qt-quickstart"
    "ffprobe",
]

uuid = "ffmpeg"

def commands():
    env.PATH.append('{root}/bin')
