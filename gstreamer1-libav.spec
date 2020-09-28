Name:           gstreamer1-libav
Version:        1.18.0
Release:        1%{?dist}
Summary:        GStreamer 1.0 libav-based plug-ins
Group:          Applications/Multimedia
License:        LGPLv2+
URL:            http://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gst-libav/gst-libav-%{version}.tar.xz
# Thanks to Jana Saout; See https://bugzilla.gnome.org/show_bug.cgi?id=789193
#Patch:          _viddec.patch
#Patch0:	        external-ffmpeg4-dep.patch
BuildRequires:  gstreamer-dev
BuildRequires:  gst-plugins-base-dev
BuildRequires:  orc-dev
BuildRequires:  bzip2-dev
BuildRequires:  zlib-dev
BuildRequires:  ffmpeg-dev
BuildRequires:  yasm
BuildRequires:  meson


%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package provides libav-based GStreamer plug-ins.


%package dev-docs
Summary: Development documentation for the libav GStreamer plug-in
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description dev-docs
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains the development documentation for the libav GStreamer
plug-in.


%prep
%setup -n gst-libav-%{version} 


%build
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572633870
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -Wno-deprecated-declarations "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool

meson  \ 
   --libdir=lib64 --prefix=/usr \
   --buildtype=plain \ 
   -D package-name="gst-libav clearfraction" \
   -D package-origin="https://github.com/clearfraction" \
   -D doc=disabled \
   builddir

ninja -v -C builddir
    
    
%install
DESTDIR=%{buildroot} ninja -C builddir install



%files
%{_libdir}/gstreamer-1.0/libgstlibav.so

%files dev-docs
# Take the dir and everything below it for proper dir ownership
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING.LIB
%doc %{_datadir}/gtk-doc


%changelog
# based on https://github.com/UnitedRPMs/gstreamer1-libav
