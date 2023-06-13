Summary:	Collection of GStreamer video effects
Summary(pl.UTF-8):	Zestaw efektów wideo GStreamera
Name:		gnome-video-effects
Version:	0.6.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	https://download.gnome.org/sources/gnome-video-effects/0.6/%{name}-%{version}.tar.xz
# Source0-md5:	dd2b93c3da1aad22a2e3e3e44402f3d6
URL:		https://wiki.gnome.org/Projects/GnomeVideoEffects
BuildRequires:	gettext-tools
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of GStreamer effects to be used in different GNOME
Modules.

%description -l pl.UTF-8
Zestaw efektów GStreamera do użycia w różnych modułach GNOME.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%{_datadir}/gnome-video-effects
%{_npkgconfigdir}/gnome-video-effects.pc
