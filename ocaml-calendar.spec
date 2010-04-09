%define up_name	calendar
%define name	ocaml-%{up_name}
%define version	2.02
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Ocaml calendar library
License:	GPL
Group:		Development/Other
URL:		http://forge.ocamlcore.org/projects/calendar/
Source0:	http://forge.ocamlcore.org/frs/download.php/333/%{up_name}-%{version}.tar.gz
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The Calendar library is a library providing a set of operations over dates and
times.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n %{up_name}-%{version}

%build
%configure2_5x
%make
sed -i -e 's/calendarLib.cmo //g' META
sed -i -e 's/calendarLib.cmx //g' META

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_libdir}/ocaml
make install OCAMLFIND_DESTDIR="%{buildroot}%{_libdir}/ocaml"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc calendarFAQ-2.6.txt calendar_faq.txt CHANGES COPYING LGPL README TODO
%dir %{_libdir}/ocaml/calendar
%{_libdir}/ocaml/calendar/*.cmi
%{_libdir}/ocaml/calendar/*.cmo

%files devel
%defattr(-,root,root)
%{_libdir}/ocaml/calendar/*
%exclude %{_libdir}/ocaml/calendar/*.cmi
%exclude %{_libdir}/ocaml/calendar/*.cmo
