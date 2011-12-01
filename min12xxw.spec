Name:           min12xxw
Version:        0.0.9
Release:        5.1%{?dist}
Summary:        Converts PBM stream to Minolta printer language

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://www.hinterbergen.de/mala/min12xxw/
Source0:        http://www.hinterbergen.de/mala/min12xxw/min12xxw-0.0.9.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#Though it includes no translations, who this doesn't matter really for now.
#The translation of both the package and SPEC (Summary and %desciption) are
#considered a TODO
#BuildRequires:  gettext

%description
This is a filter to convert pbmraw data such as produced by ghostscript to
the printer language of Minolta 1[234]xx W printers. It is meant to be used
by the PostScript Description files of the drivers from the foomatic package.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/esc-m
%{_bindir}/min12xxw
%{_mandir}/man1/min12xxw.1.gz
%doc AUTHORS ChangeLog NEWS README COPYING format.txt

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.0.9-5.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0.9-3
- Autorebuild for GCC 4.3

* Fri Aug 3 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.0.9-2
- Modify the License tag in accordance with the new guidelines

* Wed Jun 6 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.0.9-1
- Initial package
