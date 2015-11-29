%define		module	encutils
Summary:	A collection of helper functions to detect encodings of text files
Summary(pl.UTF-8):	Kolekcja funkcji wykrywającej kodowanie plików tekstowych
Name:		python-%{module}
Version:	0.9
Release:	2
License:	LGPL v2.1
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/e/encutils/%{module}-%{version}.zip
# Source0-md5:	d6b01d11bf0897e50e11d6f95b8d9b81
URL:		http://cthedot.de/encutils/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	unzip
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of helper functions to detect encodings of text files
(like HTML, XHTML, XML, CSS, etc.) retrieved via HTTP, file or string.

%description -l pl.UTF-8
Kolekcja funkcji wykrywającej kodowanie plików tekstowych (HTML,
XHTML, XML, CSS, etc.) pobranych przez HTTP, plik lub ciąg znaków.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install \
        --single-version-externally-managed \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%dir %{py_sitescriptdir}/encutils
%attr(755,root,root) %{py_sitescriptdir}/encutils/*.py[co]
%{py_sitescriptdir}/*.egg-info
