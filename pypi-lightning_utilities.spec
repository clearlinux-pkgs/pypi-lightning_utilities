#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-lightning_utilities
Version  : 0.9.0
Release  : 2
URL      : https://files.pythonhosted.org/packages/dd/c0/0850bf9930c85ec68153e096662735bc1df2e4dab9acb469e2dfa72a0f9a/lightning-utilities-0.9.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/dd/c0/0850bf9930c85ec68153e096662735bc1df2e4dab9acb469e2dfa72a0f9a/lightning-utilities-0.9.0.tar.gz
Summary  : PyTorch Lightning Sample project.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-lightning_utilities-license = %{version}-%{release}
Requires: pypi-lightning_utilities-python = %{version}-%{release}
Requires: pypi-lightning_utilities-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Lightning Utilities
[![UnitTests](https://github.com/Lightning-AI/utilities/actions/workflows/ci-testing.yml/badge.svg?event=push)](https://github.com/Lightning-AI/utilities/actions/workflows/ci-testing.yml)
[![Apply checks](https://github.com/Lightning-AI/utilities/actions/workflows/ci-use-checks.yaml/badge.svg?event=push)](https://github.com/Lightning-AI/utilities/actions/workflows/ci-use-checks.yaml)
[![Docs Status](https://readthedocs.org/projects/lit-utilities/badge/?version=latest)](https://lit-utilities.readthedocs.io/en/latest/?badge=latest)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Lightning-AI/utilities/main.svg)](https://results.pre-commit.ci/latest/github/Lightning-AI/utilities/main)

%package license
Summary: license components for the pypi-lightning_utilities package.
Group: Default

%description license
license components for the pypi-lightning_utilities package.


%package python
Summary: python components for the pypi-lightning_utilities package.
Group: Default
Requires: pypi-lightning_utilities-python3 = %{version}-%{release}

%description python
python components for the pypi-lightning_utilities package.


%package python3
Summary: python3 components for the pypi-lightning_utilities package.
Group: Default
Requires: python3-core
Provides: pypi(lightning_utilities)
Requires: pypi(packaging)
Requires: pypi(typing_extensions)

%description python3
python3 components for the pypi-lightning_utilities package.


%prep
%setup -q -n lightning-utilities-0.9.0
cd %{_builddir}/lightning-utilities-0.9.0
pushd ..
cp -a lightning-utilities-0.9.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688138548
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-lightning_utilities
cp %{_builddir}/lightning-utilities-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-lightning_utilities/17b8e993f550aa9ab2ab6ac19ffab455c6d9661d || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-lightning_utilities/17b8e993f550aa9ab2ab6ac19ffab455c6d9661d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
