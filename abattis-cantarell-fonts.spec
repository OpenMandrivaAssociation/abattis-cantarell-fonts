%define oname		cantarell-fonts
%define fontconf	31-cantarell.conf

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Cantarell, a Humanist sans-serif font family
Name:		abattis-%{oname}
Version:	0.0.12
Release:	7
Group:		System/Fonts/True type 
License:	OFL
URL:		http://abattis.org/cantarell/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/cantarell-fonts/%{url_ver}/%{oname}-%{version}.tar.xz

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

