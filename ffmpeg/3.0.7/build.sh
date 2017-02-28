#!/usr/bin/bash

build_dir=$1
install_dir=$2
archive_dir=$3
ffmpeg_ver=$4

cd ${build_dir}

# YASM
git clone --depth 1 git://github.com/yasm/yasm.git
cd yasm
autoreconf -fiv
./configure --prefix="${build_dir}/ffmpeg_build" --bindir="${build_dir}/ffmpeg_build/bin"
make install
# make distclean

# libx264
cd ${build_dir}
git clone --depth 1 git://git.videolan.org/x264
cd x264
PATH=${PATH}:${build_dir}/ffmpeg_build/bin ./configure --prefix="${build_dir}/ffmpeg_build" --bindir="${build_dir}/bin" --enable-static
PATH=${PATH}:${build_dir}/ffmpeg_build/bin make
make install
# make distclean

# libx265
cd ${build_dir}
hg clone https://bitbucket.org/multicoreware/x265
cd ./x265/build/linux
cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX="${build_dir}/ffmpeg_build" -DENABLE_SHARED:bool=off ../../source
make install

# libmp3lame
cd ${build_dir}
curl -L -O http://downloads.sourceforge.net/project/lame/lame/3.99/lame-3.99.5.tar.gz
tar xzvf lame-3.99.5.tar.gz
cd lame-3.99.5
./configure --prefix="${build_dir}/ffmpeg_build" --bindir="$HOME/bin" --disable-shared --enable-nasm
make install
# make distclean

# libfdk_aac
cd ${build_dir}
git clone --depth 1 git://git.code.sf.net/p/opencore-amr/fdk-aac
cd fdk-aac
autoreconf -fiv
./configure --prefix="${build_dir}/ffmpeg_build" --disable-shared
make install
# make distclean

# libopus
cd ${build_dir}
git clone git://git.opus-codec.org/opus.git
cd opus
autoreconf -fiv
./configure --prefix="${build_dir}/ffmpeg_build" --disable-shared
make install
make distclean

# libogg
cd ${build_dir}
curl -O http://downloads.xiph.org/releases/ogg/libogg-1.3.2.tar.gz
tar xzvf libogg-1.3.2.tar.gz
cd libogg-1.3.2
./configure --prefix="${build_dir}/ffmpeg_build" --disable-shared
make install
# make distclean

#libvorbis
cd ${build_dir}
curl -O http://downloads.xiph.org/releases/vorbis/libvorbis-1.3.4.tar.gz
tar xzvf libvorbis-1.3.4.tar.gz
cd libvorbis-1.3.4
LDFLAGS="-L$HOME/ffmeg_build/lib" CPPFLAGS="-I${build_dir}/ffmpeg_build/include" ./configure --prefix="${build_dir}/ffmpeg_build" --with-ogg="${build_dir}/ffmpeg_build" --disable-shared
make install
# make distclean

# libvpx
cd ${build_dir}
git clone --depth 1 https://chromium.googlesource.com/webm/libvpx.git
cd libvpx
PATH=${PATH}:${build_dir}/ffmpeg_build/bin ./configure --prefix="${build_dir}/ffmpeg_build" --disable-examples
PATH=${PATH}:${build_dir}/ffmpeg_build/bin make install
make clean

cd ${build_dir}
git clone -b n${ffmpeg_ver} git://github.com/FFmpeg/FFmpeg.git
mkdir objdir
cd objdir
PKG_CONFIG_PATH="${build_dir}/ffmpeg_build/lib/pkgconfig" ../FFmpeg/configure --prefix="${install_dir}" --extra-cflags="-I${build_dir}/ffmpeg_build/include" --extra-ldflags="-L${build_dir}/ffmpeg_build/lib" --bindir="${install_dir}/bin" --pkg-config-flags="--static" --enable-gpl --enable-nonfree --enable-libfdk-aac --enable-libfreetype --enable-libmp3lame --enable-libvorbis --enable-libx264 --enable-libx265
make install
make distclean
hash -r