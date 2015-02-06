%define up_name	calendar
%define name	ocaml-%{up_name}
%define version	2.02
%define release	3

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


%changelog
* Wed May 09 2012 Crispin Boylan <crisb@mandriva.org> 2.02-2
+ Revision: 797827
- Rebuild

* Fri May 07 2010 Florent Monnier <blue_prawn@mandriva.org> 2.02-1mdv2011.0
+ Revision: 543157
- removed old tarball

* Fri Apr 09 2010 Florent Monnier <blue_prawn@mandriva.org> 2.02-1mdv2010.1
+ Revision: 533482
- updated to version 2.02

* Fri Jul 31 2009 Florent Monnier <blue_prawn@mandriva.org> 2.01.1-3mdv2010.0
+ Revision: 405217
- incremented rel number
- corrected META file

* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.01.1-2mdv2010.0
+ Revision: 390236
- rebuild

* Sat May 23 2009 Florent Monnier <blue_prawn@mandriva.org> 2.01.1-1mdv2010.0
+ Revision: 379074
- updated version
- updated version

* Wed Dec 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.4-4mdv2009.1
+ Revision: 318258
- site-lib hierarchy doesn't exists anymore

* Sun Dec 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.4-3mdv2009.1
+ Revision: 317098
- move .cmo files in non-devel package (contributed by Florent Monnier <fmonnier@linux-nantes.org>

* Tue Dec 09 2008 Pixel <pixel@mandriva.com> 2.0.4-2mdv2009.1
+ Revision: 312242
- rebuild

* Thu Aug 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.4-1mdv2009.0
+ Revision: 272054
- new version, drop destdir patch

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.10-5mdv2009.0
+ Revision: 254180
- rebuild

* Tue Mar 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-3mdv2008.1
+ Revision: 178362
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-2mdv2008.0
+ Revision: 77642
- drop macro definition, now in rpm-mandriva-setup
  ship .cmi file in non-devel subpackage

* Tue Jun 19 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.10-1mdv2008.0
+ Revision: 41235
- new release: 1.10

* Thu Apr 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.09.6-1mdv2008.0
+ Revision: 18422
- Import ocaml-calendar

