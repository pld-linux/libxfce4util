#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	static_libs	# don't build static library
#
Summary:	Utility library for the Xfce desktop environment
Summary(pl.UTF-8):	Biblioteka narzędziowa dla środowiska Xfce
Name:		libxfce4util
Version:	4.6.2
Release:	2
License:	BSD, LGPL
Group:		Libraries
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	9c3129d827d480f0906c575e7a13f1e9
URL:		http://www.xfce.org/projects/libraries/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.12.4
BuildRequires:	gtk-doc-automake
%{?with_apidocs:BuildRequires:	gtk-doc}
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	xfce4-dev-tools >= 4.6.0
Requires:	xfce4-dirs >= 4.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Basic utility non-GUI functions for Xfce.

%description -l pl.UTF-8
Podstawowe funkcje narzędziowe nie związane z GUI dla Xfce.

%package apidocs
Summary:	libxfce4util API documentation
Summary(pl.UTF-8):	Dokumentacja API libxfce4util
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libxfce4util API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libxfce4util.

%package devel
Summary:	Development files for libxfce4util library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libxfce4util
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.12.4

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

%package tools
Summary:	Tools for libxfce4util library
Summary(pl.UTF-8):	Narzędzia biblioteki libxfce4util
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description tools
Tools for libxfce4util library.

%description static -l pl.UTF-8
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
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}/libxfce4util}

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README NEWS THANKS TODO
%attr(755,root,root) %{_libdir}/libxfce4util.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfce4util.so.4

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfce4util.so
%{_libdir}/libxfce4util.la
%dir %{_includedir}/xfce4
%{_includedir}/xfce4/libxfce4util
%{_pkgconfigdir}/libxfce4util-1.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libxfce4util.a
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/xfce4-kiosk-query
