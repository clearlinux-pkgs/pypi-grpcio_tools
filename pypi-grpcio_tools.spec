#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-grpcio_tools
Version  : 1.49.1
Release  : 30
URL      : https://files.pythonhosted.org/packages/6c/e4/3416d25aebc4477141a491fae2c9494c5e0437a706c59103a936aac7d072/grpcio-tools-1.49.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/6c/e4/3416d25aebc4477141a491fae2c9494c5e0437a706c59103a936aac7d072/grpcio-tools-1.49.1.tar.gz
Summary  : Protobuf code generator for gRPC
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-grpcio_tools-filemap = %{version}-%{release}
Requires: pypi-grpcio_tools-lib = %{version}-%{release}
Requires: pypi-grpcio_tools-python = %{version}-%{release}
Requires: pypi-grpcio_tools-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(grpcio)
BuildRequires : pypi(protobuf)
BuildRequires : pypi(setuptools)

%description
=================
        
        Package for gRPC Python tools.
        
        Supported Python Versions
        -------------------------
        Python >= 3.6
        
        Installation
        ------------
        
        The gRPC Python tools package is available for Linux, Mac OS X, and Windows.
        
        Installing From PyPI
        ~~~~~~~~~~~~~~~~~~~~
        
        If you are installing locally...

%package filemap
Summary: filemap components for the pypi-grpcio_tools package.
Group: Default

%description filemap
filemap components for the pypi-grpcio_tools package.


%package lib
Summary: lib components for the pypi-grpcio_tools package.
Group: Libraries
Requires: pypi-grpcio_tools-filemap = %{version}-%{release}

%description lib
lib components for the pypi-grpcio_tools package.


%package python
Summary: python components for the pypi-grpcio_tools package.
Group: Default
Requires: pypi-grpcio_tools-python3 = %{version}-%{release}

%description python
python components for the pypi-grpcio_tools package.


%package python3
Summary: python3 components for the pypi-grpcio_tools package.
Group: Default
Requires: pypi-grpcio_tools-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(grpcio_tools)
Requires: pypi(grpcio)
Requires: pypi(protobuf)
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-grpcio_tools package.


%prep
%setup -q -n grpcio-tools-1.49.1
cd %{_builddir}/grpcio-tools-1.49.1
pushd ..
cp -a grpcio-tools-1.49.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663862312
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-grpcio_tools

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
