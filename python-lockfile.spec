# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-lockfile
Epoch: 100
Version: 0.12.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Platform-independent file locking module
License: MIT
URL: https://github.com/openstack-archive/pylockfile/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
The lockfile module exports a FileLock class which provides a simple API
for locking files. Unlike the Windows msvcrt.locking function, the Unix
fcntl.flock, fcntl.lockf and the deprecated posixfile module, the API is
identical across both Unix (including Linux and Mac) and Windows
platforms. The lock mechanism relies on the atomic nature of the link
(on Unix) and mkdir (on Windows) system calls.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500 || 0%{?rhel} == 7
%package -n python%{python3_version_nodots}-lockfile
Summary: Platform-independent file locking module
Requires: python3
Provides: python3-lockfile = %{epoch}:%{version}-%{release}
Provides: python3dist(lockfile) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-lockfile = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(lockfile) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-lockfile = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(lockfile) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-lockfile
The lockfile module exports a FileLock class which provides a simple API
for locking files. Unlike the Windows msvcrt.locking function, the Unix
fcntl.flock, fcntl.lockf and the deprecated posixfile module, the API is
identical across both Unix (including Linux and Mac) and Windows
platforms. The lock mechanism relies on the atomic nature of the link
(on Unix) and mkdir (on Windows) system calls.

%files -n python%{python3_version_nodots}-lockfile
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?rhel} == 7)
%package -n python3-lockfile
Summary: Platform-independent file locking module
Requires: python3
Provides: python3-lockfile = %{epoch}:%{version}-%{release}
Provides: python3dist(lockfile) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-lockfile = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(lockfile) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-lockfile = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(lockfile) = %{epoch}:%{version}-%{release}

%description -n python3-lockfile
The lockfile module exports a FileLock class which provides a simple API
for locking files. Unlike the Windows msvcrt.locking function, the Unix
fcntl.flock, fcntl.lockf and the deprecated posixfile module, the API is
identical across both Unix (including Linux and Mac) and Windows
platforms. The lock mechanism relies on the atomic nature of the link
(on Unix) and mkdir (on Windows) system calls.

%files -n python3-lockfile
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
