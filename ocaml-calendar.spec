%define up_name	calendar
%define name	ocaml-%{up_name}
%define version	1.09.6
%define release	%mkrel 1
%define ocaml_sitelib %(if [ -x /usr/bin/ocamlc ]; then ocamlc -where;fi)/site-lib

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Ocaml calendar library
License:	GPL
Group:		Development/Other
URL:		http://www.lri.fr/~signoles/prog/calendar/
Source: 	http://www.lri.fr/~signoles/prog/calendar/%{up_name}-%{version}.tar.bz2
Patch: 	    %{name}-%{version}-destdir.patch
BuildRequires:	ocaml
BuildRequires:	findlib
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
The Calendar library is a library providing a set of operations over dates and
times.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n %{up_name}-%{version}
%patch

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{ocaml_sitelib}
make install OCAMLFIND_INSTFLAGS="-destdir %{buildroot}/%{ocaml_sitelib}"

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc calendarFAQ-2.6.txt calendar_faq.txt CHANGES COPYING LGPL README TODO
%{ocaml_sitelib}/calendar
