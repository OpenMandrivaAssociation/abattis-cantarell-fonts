%bcond_with prebuilt

%define oname		cantarell-fonts
%define fontname	cantarell
%define fontconf	31-cantarell.conf

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		abattis-%{oname}
Version:	0.201
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
BuildRequires:	python3-afdko
%if %{without prebuilt}
BuildRequires:	fontmake
BuildRequires:	psautohint >= 2.0.0
BuildRequires:	python3dist(afdko)
BuildRequires:	python3dist(cattrs)
BuildRequires:	python3dist(statmake)
BuildRequires:	python3dist(attrs)
BuildRequires:	python3dist(skia-pathops)
BuildRequires:	python3dist(ufolib2)
%endif
Requires:	fontpackages-filesystem

%description
The Cantarell font family is a contemporary Humanist sans serif
designed for on-screen reading.

%prep
%autosetup -n %{oname}-%{version} -p1

%build
%meson -Duseprebuilt=%{?with_prebuilt:true}%{?!with_prebuilt:false}
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
