#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Utility library for the Xfce desktop environment
Summary(pl):	Biblioteka narzêdziowa dla ¶rodowiska Xfce
Name:		libxfce4util
Version:	4.4.0
Release:	1
License:	BSD, LGPL
Group:		Libraries
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	543fb8efe96d6e83f897a7c64c48e9e6
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.12.4
BuildRequires:	gtk-doc-automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	xfce4-dev-tools >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Basic utility non-GUI functions for Xfce.

%description -l pl
Podstawowe funkcje narzêdziowe nie zwi±zane z GUI dla Xfce.

%package apidocs
Summary:	libxfce4util API documentation
Summary(pl):	Dokumentacja API libxfce4util
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libxfce4util API documentation.

%description apidocs -l pl
Dokumentacja API libxfce4util.

%package devel
Summary:	Development files for libxfce4util library
Summary(pl):	Pliki nag³ówkowe biblioteki libxfce4util
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.12.4

%description devel
Development files for the libxfce4util library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libxfce4util.

%package static
Summary:	Static libxfce4util library
Summary(pl):	Statyczna biblioteka libxfce4util
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libxfce4util library.

%description static -l pl
Statyczna biblioteka libxfce4util.

%package tools
Summary:	Tools for libxfce4util library
Summary(pl):	Narzêdzia biblioteki libxfce4util
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description tools
Tools for libxfce4util library.

%description static -l pl
Narzêdzia biblioteki libxfce4util.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-gtkdoc \
	--with-html-dir=%{_gtkdocdir} \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/xfce4

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README NEWS THANKS TODO
%attr(755,root,root) %{_libdir}/libxfce4util.so.*.*.*
%dir %{_datadir}/xfce4

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfce4util.so
%{_libdir}/libxfce4util.la
%dir %{_includedir}/xfce4
%{_includedir}/xfce4/libxfce4util
%{_pkgconfigdir}/*.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libxfce4util.a
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/xfce4-kiosk-query
