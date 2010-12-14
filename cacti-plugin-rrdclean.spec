%define		plugin rrdclean
Summary:	Cacti RRD File Cleaner
Name:		cacti-plugin-%{plugin}
Version:	0.40
Release:	0.4
License:	GPL v2
Group:		Applications/WWW
Source0:	http://docs.cacti.net/_media/plugin:rrdclean-v%{version}.tgz
# Source0-md5:	afd7ae246482fbee883485e0430041e8
Patch0:		paths.patch
Patch1:		fix-paths-handling.patch
URL:		http://docs.cacti.net/plugin:rrdclean
Requires:	cacti >= 0.8.6j
Requires:	php-common >= 3:4.3.0
Provides:	cacti(pia) >= 2.8
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
mv %{plugin}/* .; rmdir %{plugin}
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{plugindir},%{rradir}/{backup,archive}}
cp -a . $RPM_BUILD_ROOT%{plugindir}
%{__rm} $RPM_BUILD_ROOT%{plugindir}/{README,LICENSE}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{plugindir}
%attr(770,root,http) %dir %{rradir}/archive
%attr(770,root,http) %dir %{rradir}/backup
