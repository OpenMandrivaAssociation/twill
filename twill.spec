Name:		twill
Summary:	Simple command line language for web browsing
Version:	0.9
Release:	%{mkrel 2}
Source0:	http://darcs.idyll.org/~t/projects/%{name}-%{version}.tar.gz
URL:		http://twill.idyll.org
Group:		Networking/WWW
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	MIT
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-setuptools
Requires:	python

%description
twill is a simple language that allows users to browse the Web from a
command-line interface. With twill, you can navigate through Web sites
that use forms, cookies, and most standard Web features.

%prep
%setup -q

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.html README.txt doc/*.*
%{_bindir}/twill-fork
%{_bindir}/twill-sh
%{py_puresitedir}/%{name}-%{version}-py%{pyver}.egg-info
%{py_puresitedir}/%{name}

