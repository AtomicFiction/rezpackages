#!/usr/bin/bash

build_dir=$1
install_dir=$2
archive_dir=$3
ffmpeg_ver=$4

cd ${build_dir}
# YASM
mkdir yasm
cd yasm
tar -xvf ${REZ_REPO_PAYLOAD_DIR}/ffmpeg/yasm-1.3.0.tar.gz --strip-components=1 -C ./
autoreconf -fiv
./configure --prefix="${build_dir}/ffmpeg_build" --bindir="${build_dir}/ffmpeg_build/bin"
make install
# make distclean

# libx264
cd ${build_dir}
mkdir libx264
cd libx264
tar -xvf ${REZ_REPO_PAYLOAD_DIR}/ffmpeg/last_x264.tar.bz2 --strip-components=1 -C ./
PATH=${PATH}:${build_dir}/ffmpeg_build/bin ./configure --prefix="${build_dir}/ffmpeg_build" --bindir="${build_dir}/bin" --enable-static
PATH=${PATH}:${build_dir}/ffmpeg_build/bin make
make install
# make distclean

# libx265
cd ${build_dir}
mkdir libx265
cd libx265
tar -xvf ${REZ_REPO_PAYLOAD_DIR}/ffmpeg/x265-2.3.tar.gz --strip-components=1 -C ./
cd ./build/linux
cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX="${build_dir}/ffmpeg_build" -DENABLE_SHARED:bool=off ../../source
make install

# libmp3lame
cd ${build_dir}
mkdir lame
cd lame
tar -xvf ${REZ_REPO_PAYLOAD_DIR}/ffmpeg/lame-3.99.5.tar.gz --strip-components=1 -C ./
./configure --prefix="${build_dir}/ffmpeg_build" --bindir="$HOME/bin" --disable-shared --enable-nasm
make install
# make distclean

# libfdk_aac
cd ${build_dir}
mkdir libfdk_aac
cd libfdk_aac
tar -xvf ${REZ_REPO_PAYLOAD_DIR}/ffmpeg/fdk-aac-0.1.5.tar.gz --strip-components=1 -C ./
autoreconf -fiv
./configure --prefix="${build_dir}/ffmpeg_build" --disable-shared
make install
# make distclean

# libopus
cd ${build_dir}
mkdir opus
cd opus
tar -xvf ${REZ_REPO_PAYLOAD_DIR}/ffmpeg/opus-1.1.4.tar.gz --strip-components=1 -C ./
autoreconf -fiv
./configure --prefix="${build_dir}/ffmpeg_build" --disable-shared
make install
make distclean

# libogg
cd ${build_dir}
mkdir libogg
cd libogg
tar -xvf ${REZ_REPO_PAYLOAD_DIR}/ffmpeg/libogg-1.3.2.tar.gz --strip-components=1 -C ./
./configure --prefix="${build_dir}/ffmpeg_build" --disable-shared
make install
# make distclean

#libvorbis
cd ${build_dir}
mkdir libvorbis
cd libvorbis
tar -xvf ${REZ_REPO_PAYLOAD_DIR}/ffmpeg/libvorbis-1.3.4.tar.gz --strip-components=1 -C ./
LDFLAGS="-L$HOME/ffmeg_build/lib" CPPFLAGS="-I${build_dir}/ffmpeg_build/include" ./configure --prefix="${build_dir}/ffmpeg_build" --with-ogg="${build_dir}/ffmpeg_build" --disable-shared
make install
# make distclean

# libvpx
cd ${build_dir}
mkdir libvpx
cd libvpx
tar -xvf ${REZ_REPO_PAYLOAD_DIR}/ffmpeg/libvpx-1.6.1.tar.gz --strip-components=1 -C ./
PATH=${PATH}:${build_dir}/ffmpeg_build/bin ./configure --prefix="${build_dir}/ffmpeg_build" --disable-examples
PATH=${PATH}:${build_dir}/ffmpeg_build/bin make install
make clean

# FFmpeg
cd ${build_dir}
mkdir ffmpeg
cd ffmpeg
tar -xvf ${REZ_REPO_PAYLOAD_DIR}/ffmpeg/ffmpeg-3.0.7.tar.gz --strip-components=1 -C ./

mkdir -p objdir
cd objdir
PKG_CONFIG_PATH="${build_dir}/ffmpeg_build/lib/pkgconfig" ../configure --prefix="${install_dir}" --extra-cflags="-I${build_dir}/ffmpeg_build/include" --extra-ldflags="-L${build_dir}/ffmpeg_build/lib" --bindir="${install_dir}/bin" --pkg-config-flags="--static" --enable-gpl --enable-nonfree --enable-libfdk-aac --enable-libfreetype --enable-libmp3lame --enable-libvorbis --enable-libx264 --enable-libx265
make install
make distclean
hash -r
