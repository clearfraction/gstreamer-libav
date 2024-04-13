Name:           gstreamer1-libav
Version:        1.24.2
Release:        1%{?dist}
Summary:        GStreamer 1.0 libav-based plug-ins
Group:          Applications/Multimedia
License:        LGPLv2+
URL:            http://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gst-libav/gst-libav-%{version}.tar.xz
BuildRequires:  gstreamer-dev
BuildRequires:  gst-plugins-base-dev
BuildRequires:  orc-dev
BuildRequires:  bzip2-dev
BuildRequires:  zlib-dev
BuildRequires:  not-ffmpeg-dev
BuildRequires:  yasm
BuildRequires:  meson

%description
libav gstreamer plugins

%prep
%setup -n gst-libav-%{version} 

%build
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
 
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson \
    --libdir=lib64 --prefix=/usr \
    --buildtype=plain \
    -D package-name="gst-libav plugin compiled by ClearFraction" \
    -D package-origin="https://github.com/clearfraction" \
    -D doc=disabled builddir 

ninja -v -C builddir
    
    
%install
DESTDIR=%{buildroot} ninja -C builddir install

%files
%{_libdir}/gstreamer-1.0/libgstlibav.so

%changelog
# based on https://github.com/UnitedRPMs/gstreamer1-libav
