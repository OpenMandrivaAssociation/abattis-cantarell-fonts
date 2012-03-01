%define oname		cantarell-fonts
%define fontconf	31-cantarell.conf

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		abattis-%{oname}
Version:	0.0.7
Release:	%mkrel 1
Summary:	Cantarell, a Humanist sans-serif font family
Group:		System/Fonts/True type 
License:	OFL
URL:		http://abattis.org/cantarell/
Source0:	http://download.gnome.org/sources/%{oname}/%{url_ver}/%{oname}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	fontforge
Requires:	fontpackages-filesystem

#Obsolete wrongly imported duplicate pkg
Obsoletes:	%{oname}

%description
Cantarell is a set of fonts designed by Dave Crossland. It is a 
sans-serif humanist typeface family.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x
%make

#create fonts from "source"
fontforge -lang=ff -c 'Open($1); Generate($2);' src/Cantarell-Bold.sfd Cantarell-Bold.otf
fontforge -lang=ff -c 'Open($1); Generate($2);' src/Cantarell-Regular.sfd Cantarell-Regular.otf

%install
rm -rf %{buildroot}
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -Dpm 0644 fontconfig/%{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%clean
rm -rf %{buildroot}

%_font_pkg -f %{fontconf} *.otf
%doc COPYING NEWS README


