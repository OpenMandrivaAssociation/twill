Name:		twill
Summary:	Simple command line language for web browsing
Version:	0.9
Release:	6
Source0:	http://darcs.idyll.org/~t/projects/%{name}-%{version}.tar.gz
URL:		http://twill.idyll.org
Group:		Networking/WWW
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
%__python setup.py install --root=%{buildroot}

%files
%defattr(-,root,root)
%doc README.html README.txt doc/*.*
%{_bindir}/twill-fork
%{_bindir}/twill-sh
%{py_puresitedir}/%{name}-%{version}-py%{py_ver}.egg-info
%{py_puresitedir}/%{name}



%changelog
* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.9-4mdv2011.0
+ Revision: 592160
- rebuild for python 2.7

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.9-3mdv2010.0
+ Revision: 445569
- rebuild

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 0.9-2mdv2009.1
+ Revision: 319728
- rebuild with python 2.6

* Thu Apr 17 2008 Adam Williamson <awilliamson@mandriva.org> 0.9-1mdv2009.0
+ Revision: 195041
- import twill


