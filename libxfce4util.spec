#
# Conditional build:
%bcond_without	apidocs		# gtk-doc documentation
%bcond_with	static_libs	# static library

%define		xfce_version	4.12.0
Summary:	Utility library for the Xfce desktop environment
Summary(pl.UTF-8):	Biblioteka narzędziowa dla środowiska Xfce
Name:		libxfce4util
Version:	4.12.1
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://archive.xfce.org/src/xfce/libxfce4util/4.12/%{name}-%{version}.tar.bz2
# Source0-md5:	4eb012b6c1292ceedb3a83ebfc1ff08d
URL:		http://www.xfce.org/projects/libxfce4
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.30.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.0}
BuildRequires:	gtk-doc-automake >= 1.0
BuildRequires:	intltool >= 0.31
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
Requires:	glib2 >= 1:2.30.0
Requires:	xfce4-dirs >= 4.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Basic utility non-GUI functions for Xfce.

%description -l pl.UTF-8
Podstawowe funkcje narzędziowe nie związane z GUI dla Xfce.

%package devel
Summary:	Development files for libxfce4util library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libxfce4util
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.30.0

%description devel
Development files for the libxfce4util library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libxfce4util.

%package static
Summary:	Static libxfce4util library
Summary(pl.UTF-8):	Statyczna biblioteka libxfce4util
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libxfce4util library.

%description static -l pl.UTF-8
Statyczna biblioteka libxfce4util.

%package apidocs
Summary:	libxfce4util API documentation
Summary(pl.UTF-8):	Dokumentacja API libxfce4util
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
libxfce4util API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libxfce4util.

%package tools
Summary:	Tools for libxfce4util library
Summary(pl.UTF-8):	Narzędzia biblioteki libxfce4util
License:	GPL v2+
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description tools
Tools for libxfce4util library.

%description tools -l pl.UTF-8
Narzędzia biblioteki libxfce4util.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-gtk-doc%{!?with_apidocs:=no} \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}/libxfce4util}

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
# just a copy of ur
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/libxfce4util.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfce4util.so.7

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfce4util.so
%dir %{_includedir}/xfce4
%{_includedir}/xfce4/libxfce4util
%{_pkgconfigdir}/libxfce4util-1.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libxfce4util.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/xfce4-kiosk-query
