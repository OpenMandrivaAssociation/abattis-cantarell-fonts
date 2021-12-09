%define oname cantarell-fonts
%define fontname cantarell
%define fontconf 31-cantarell.conf

%define url_ver %(echo %{version}|cut -d. -f1,2)

Name:		abattis-%{oname}
Version:	0.303
Release:	1
Summary:	Humanist sans-serif font family
Group:		System/Fonts/True type
License:	OFL
URL:		https://gitlab.gnome.org/GNOME/cantarell-fonts/
Source0:	https://download.gnome.org/sources/%{oname}/%{url_ver}/%{oname}-%{version}.tar.xz
Source1:	cantarell-fontconfig.conf
BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	meson
BuildRequires:	appstream
BuildRequires:  python3dist(psautohint)
Requires:	fontpackages-filesystem

%description
The Cantarell font family is a contemporary Humanist sans serif
designed for on-screen reading.

%prep
%autosetup -n %{oname}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f %{fontconf} *.otf
%license COPYING
%doc NEWS README.md
%{_metainfodir}/org.gnome.cantarell.metainfo.xml
