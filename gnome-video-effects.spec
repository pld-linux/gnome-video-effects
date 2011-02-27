Summary:	Collection of GStreamer video effects
Summary(pl.UTF-8):	Zestaw efektów wideo GStreamera
Name:		gnome-video-effects
Version:	0.2.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-video-effects/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	b0fd0a14c908dbb2e23fd599fa7a9f34
URL:		http://live.gnome.org/GnomeVideoEffects
BuildRequires:	gettext-devel
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
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/gnome-video-effects
%{_npkgconfigdir}/gnome-video-effects.pc
