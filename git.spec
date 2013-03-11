Name: git
Version: 1.8.1.3
Release: 1
License: GPLv2
Group: Development/Tools
URL: http://github.com/git/git
Packager: Leevar Williams
Summary: Distributed revision control system

Source0: git-%{version}.tar.gz

BuildRequires: make gcc openssl-devel gettext-devel expat-devel
Requires: openssl-clients libcurl perl libexpat zlib rsync

%description
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

%prep
%setup -q

%build
rm -rf $RPM_BUILD_ROOT
make configure
./configure
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING INSTALL LGPL-2.1 RelNotes
/usr/local
