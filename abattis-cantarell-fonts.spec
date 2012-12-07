%define oname		cantarell-fonts
%define fontconf	31-cantarell.conf

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Cantarell, a Humanist sans-serif font family
Name:		abattis-%{oname}
Version: 0.0.11
Release: 0
Group:		System/Fonts/True type 
License:	OFL
URL:		http://abattis.org/cantarell/
Source0: cantarell-fonts-0.0.11.tar.xz
# Upstream patches
Patch0: cantarell-cyrillic-support.patch

BuildArch:	noarch
BuildRequires:	fontforge

%description
Cantarell is a set of fonts designed by Dave Crossland. It is a 
sans-serif humanist typeface family.

%prep
%setup -qn %{oname}-%{version}
%patch0 -p1 -b .cyrillic-support

%build
%configure2_5x
%make

#create fonts from "source"
fontforge -lang=ff -c 'Open($1); Generate($2);' src/Cantarell-Bold.sfd Cantarell-Bold.otf
fontforge -lang=ff -c 'Open($1); Generate($2);' src/Cantarell-Regular.sfd Cantarell-Regular.otf

%install
rm -rf %{buildroot}
install -m 0755 -d %{buildroot}%{_datadir}/fontconfig/conf.avail
install -m 0755 -d %{buildroot}%{_xfontdir}/%{name}
install -m 0755 -d %{buildroot}%{_sysconfdir}/fonts/conf.d

install -m 0644 -p *.otf %{buildroot}%{_xfontdir}/%{name}
install -Dpm 0644 fontconfig/%{fontconf} \
        %{buildroot}%{_datadir}/fontconfig/conf.avail

ln -s %{_datadir}/fontconfig/conf.avail/%{fontconf} \
      %{buildroot}%{_sysconfdir}/fonts/conf.d/%{fontconf}

%files
%doc COPYING NEWS README
%{_sysconfdir}/fonts/conf.d/%{fontconf} 
%{_datadir}/fontconfig/conf.avail/%{fontconf}
%{_xfontdir}/%{name}/*.otf



%changelog
* Fri Apr 27 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 0.0.8-1
- update to 0.0.8
- apply cyrillic patch

* Thu Mar 01 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.0.7-1
+ Revision: 781527
- cleaned up spec
- imported package abattis-cantarell-fonts



* Tue Oct 18 2011 wally <wally> 0.0.7-1.mga2
+ Revision: 156380
- new version 0.0.7
- clean .spec a bit

* Wed Jun 15 2011 dmorgan <dmorgan> 0.0.6-1.mga2
+ Revision: 106419
- New version 0.0.6

* Sun Mar 13 2011 dmorgan <dmorgan> 0.0.3-1.mga1
+ Revision: 70838
- imported package abattis-cantarell-fonts


* Mon Feb 21 2011 Cosimo Cecchi <cosimoc@redhat.com> - 0.0.3-1
- Update to 0.0.3

* Fri Feb 18 2011 Cosimo Cecchi <cosimoc@redhat.com> - 0.0.1-4
- Include upstream patch for the fontconfig snippet

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb  8 2011 Stephen Smoogen <ssmoogen@redhat.com> - 0.0.1-2
- Fixed to meet review standards

* Tue Feb  8 2011 Cosimo Cecchi <cosimoc@redhat.com> - 0.0.1-1
- Initial packaging of abattis-cantarell-fonts


