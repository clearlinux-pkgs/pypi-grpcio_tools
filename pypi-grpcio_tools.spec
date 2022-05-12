#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-grpcio_tools
Version  : 1.46.1
Release  : 20
URL      : https://files.pythonhosted.org/packages/f2/99/be726a40d301aaf5af15aa29a302833437f1d51fb436bb90322b17657f6c/grpcio-tools-1.46.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/f2/99/be726a40d301aaf5af15aa29a302833437f1d51fb436bb90322b17657f6c/grpcio-tools-1.46.1.tar.gz
Summary  : Protobuf code generator for gRPC
Group    : Development/Tools
License  : Apache-2.0
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

%package python
Summary: python components for the pypi-grpcio_tools package.
Group: Default
Requires: pypi-grpcio_tools-python3 = %{version}-%{release}

%description python
python components for the pypi-grpcio_tools package.


%package python3
Summary: python3 components for the pypi-grpcio_tools package.
Group: Default
Requires: python3-core
Provides: pypi(grpcio_tools)
Requires: pypi(grpcio)
Requires: pypi(protobuf)
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-grpcio_tools package.


%prep
%setup -q -n grpcio-tools-1.46.1
cd %{_builddir}/grpcio-tools-1.46.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1652398918
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

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
