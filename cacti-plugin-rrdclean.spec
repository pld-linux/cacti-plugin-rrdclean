%define		namesrc	rrdclean	
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - RRDClean
Summary(pl.UTF-8):	Wtyczka do Cacti - RRDClean
Name:		cacti-plugin-RRDClean
Version:	0.32
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
# source from:http://forums.cacti.net/about5852.html
Source0:	%{namesrc}-%{version}.tgz
# Source0-md5:	eb14850dbc27efce52939dae59b71d0d
URL:		http://cactiusers.org/wiki/RRDCleanDocs
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
RRDClean - Backup or Delete unused RRD files from the rra cacti folder
with the click of a button.

%description -l pl.UTF-8
Wtyczka do Cacti RRDClean - tworzenie kopii zapasowej lub usuwanie
nieużywanych plików RRD z folderu cacti rra za naciśnięciem przycisku.

%prep
%setup -q -n %{namesrc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README 
%{webcactipluginroot}
