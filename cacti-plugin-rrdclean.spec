%define		plugin rrdclean
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	Cacti RRD File Cleaner
Name:		cacti-plugin-%{plugin}
Version:	0.41
Release:	5
License:	GPL v2
Group:		Applications/WWW
Source0:	http://docs.cacti.net/_media/plugin:rrdclean-v%{version}.tgz
# Source0-md5:	e9dd1eeea27003ebb5239a1fa08b73ef
Patch0:		paths.patch
URL:		http://docs.cacti.net/plugin:rrdclean
Requires:	cacti >= 0.8.7
Requires:	cacti(pia) >= 2.4
Requires:	php(pcre)
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-date
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}
%define		rradir			/var/lib/cacti/rra

%description
This plugin analyzes many cacti db structures to determine unused rrd
files.

%prep
%setup -qc
cd %{plugin}
%patch0 -p1
cd ..

mv %{plugin}/{README,LICENSE} .

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{plugindir},%{rradir}/{backup,archive}}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{plugindir}
%attr(770,root,http) %dir %{rradir}/archive
%attr(770,root,http) %dir %{rradir}/backup
