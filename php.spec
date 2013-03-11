Name: php
Version: 5.4.9
Release: 1
License: PHP
Group: Development/Languages
URL: http://www.php.net
Packager: Leevar Williams
Summary: PHP scripting language for creating dynamic web sites

Source0: php-%{version}.tar.gz

BuildRequires: make gcc gcc-c++ libxml2-devel openssl-devel bzip2-devel libcurl-devel libjpeg-devel libpng-devel freetype-devel t1lib-devel gmp-devel libmcrypt-devel readline-devel net-snmp-devel libxslt-devel
Requires: libxml2 openssl bzip2 bzip2-libs libcurl libjpeg libpng freetype t1lib gmp libmcrypt readline net-snmp-libs libxslt

%description
PHP is an HTML-embedded scripting language. PHP attempts to make it
easy for developers to write dynamically generated webpages. PHP also
offers built-in database integration for several commercial and
non-commercial database management systems, so writing a
database-enabled webpage with PHP is fairly simple. The most common
use of PHP coding is probably as a replacement for CGI scripts.

%prep
%setup -q

%build
rm -rf $RPM_BUILD_ROOT
./configure --with-pear --enable-calendar --enable-bcmath --with-gmp --enable-exif --with-mcrypt --with-mhash --with-zlib --with-bz2 --enable-zip --with-curl --with-gd --with-jpeg-dir --with-png-dir --with-freetype-dir --with-t1lib --with-mysql --with-mysqli --with-pdo-mysql --with-openssl --with-xmlrpc --with-xsl --with-gettext --with-readline --with-snmp --enable-fpm --enable-cli --enable-inline-optimization --enable-wddx --enable-ftp --enable-mbstring --enable-soap --enable-sockets --enable-shmop --enable-dba --enable-sysvsem --enable-sysvshm --enable-sysvmsg --with-config-file-path=/etc/php
make

%install
make install INSTALL_ROOT=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/etc/init.d
cp %{_builddir}/%{name}-%{version}/sapi/fpm/init.d.php-fpm $RPM_BUILD_ROOT/etc/init.d/php-fpm
chmod 755 $RPM_BUILD_ROOT/etc/init.d/php-fpm

mkdir -p $RPM_BUILD_ROOT/etc/php
cp %{_builddir}/%{name}-%{version}/php.ini-production $RPM_BUILD_ROOT/etc/php/php.ini
cp %{_builddir}/%{name}-%{version}/php.ini-development $RPM_BUILD_ROOT/etc/php/php-dev.ini
chmod 644 $RPM_BUILD_ROOT/etc/php/php.ini
chmod 644 $RPM_BUILD_ROOT/etc/php/php-dev.ini

rm -rf $RPM_BUILD_ROOT/.channels
rm -rf $RPM_BUILD_ROOT/.depdb
rm -rf $RPM_BUILD_ROOT/.depdblock
rm -rf $RPM_BUILD_ROOT/.filemap
rm -rf $RPM_BUILD_ROOT/.lock

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CREDITS CODING_STANDARDS INSTALL LICENSE NEWS README.*
/etc/init.d/php-fpm
/etc/php/php.ini
/etc/php/php-dev.ini
/usr/local/include/php
/usr/local/php
/usr/local/sbin/php-fpm
/usr/local/lib/php
/usr/local/etc/php-fpm.conf.default
/usr/local/etc/pear.conf
/usr/local/bin/peardev
/usr/local/bin/php
/usr/local/bin/pecl
/usr/local/bin/pear
/usr/local/bin/php-cgi
/usr/local/bin/phar
/usr/local/bin/phar.phar
/usr/local/bin/phpize
/usr/local/bin/php-config
