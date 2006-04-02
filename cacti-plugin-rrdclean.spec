%define		namesrc	namesrc	
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - RRDClean
Summary(pl):	Wtyczka do Cacti - RRDClean
Name:		cacti-plugin-RRDClean
Version:	1.1
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://download.cactiusers.org/downloads/%{namesrc}.tar.gz
# Source0-md5:	
URL:		http://cactiusers.org/wiki/RRDCleanDocs
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
RRDClean Backup or Delete unused RRD files from the rra cacti folder 
with the click of a button.

%description -l pl
Wtyczka do Cacti - 

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
%doc LICENSE README 
%{webcactipluginroot}
