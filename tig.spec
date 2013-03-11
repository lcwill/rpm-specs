Name: tig
Version: 1.1
Release: 1
License: Gnu GPL
Group: Development/Libraries
URL: https://github.com/jonas/tig
Packager: Leevar Williams
Summary: Text-mode interface for Git

Source0: tig-%{version}.tar.gz

BuildRequires: make gcc ncurses-devel
Requires: ncurses git

%description
Tig is a git repository browser that additionally can act as a pager for output from various git commands.

%prep
%setup -q -n tig-tig-%{version}

%build
rm -rf $RPM_BUILD_ROOT
make configure
./configure --prefix=$RPM_BUILD_ROOT%{_prefix}
make

%install
make install INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING INSTALL NEWS README manual.txt
%{_bindir}/tig
