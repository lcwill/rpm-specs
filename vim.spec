Name: vim
Version: 7.2.446
Release: 1
License: VIM GPL
Group: Applications/Editors
URL: http://vim.org
Packager: Leevar Williams
Summary: Vim ("Vi IMproved") is a text editor similar to "vi"

Source0: vim-%{version}.tar.gz

BuildRequires: make gcc ncurses-devel python-devel perl-devel ruby-devel
Requires: ncurses python ruby perl

%description
VIM (VIsual editor iMproved) is an updated and improved version of the vi editor. Vi was the first real screen-based editor for UNIX, and is still very popular. VIM improves on vi by adding new features: multiple windows, multi-level undo, block highlighting and more.

%prep
%setup -q -n vim-%{version}

%build
rm -rf $RPM_BUILD_ROOT
./configure --prefix=/usr --enable-perlinterp --enable-rubyinterp --enable-pythoninterp --with-python-config-dir=/usr/lib64/python2.6/config --enable-multibyte --disable-netbeans --enable-gui=no --disable-gpm --disable-gtktest --disable-xim --without-x --with-tlib=ncurses
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.txt README_unix.txt README_src.txt README_lang.txt src/INSTALL
/usr
