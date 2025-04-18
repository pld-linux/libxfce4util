#
# Conditional build:
%bcond_without	apidocs		# gtk-doc documentation
%bcond_with	static_libs	# static library

Summary:	Utility library for the Xfce desktop environment
Summary(pl.UTF-8):	Biblioteka narzędziowa dla środowiska Xfce
Name:		libxfce4util
Version:	4.20.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://archive.xfce.org/src/xfce/libxfce4util/4.20/%{name}-%{version}.tar.bz2
# Source0-md5:	8e30b7735333f74d80c379e15d9da145
URL:		https://www.xfce.org/projects/libxfce4
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.8
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.72.0
BuildRequires:	gobject-introspection-devel >= 1.66.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.9}
BuildRequires:	gtk-doc-automake >= 1.9
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	vala
BuildRequires:	xfce4-dev-tools >= 4.20.0
Requires:	glib2 >= 1:2.72.0
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
Requires:	glib2-devel >= 1:2.72.0

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
BuildArch:	noarch

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

%package -n vala-libxfce4util
Summary:	Vala API for libxfce4util library
Summary(pl.UTF-8):	API języka Vala do biblioteki libxfce4util
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala
BuildArch:	noarch

%description -n vala-libxfce4util
Vala API for libxfce4util library.

%description -n vala-libxfce4util -l pl.UTF-8
API języka Vala do biblioteki libxfce4util.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoheader}
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

# unify to short code
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{fa_IR,fa}
# duplicates of hy,ur
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hye,hy_AM,ur_PK}
# not supported by glibc (as of 2.32)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md
%attr(755,root,root) %{_libdir}/libxfce4util.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfce4util.so.7
%{_libdir}/girepository-1.0/Libxfce4util-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfce4util.so
%dir %{_includedir}/xfce4
%{_includedir}/xfce4/libxfce4util
%{_pkgconfigdir}/libxfce4util-1.0.pc
%{_datadir}/gir-1.0/Libxfce4util-1.0.gir

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

%files -n vala-libxfce4util
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libxfce4util-1.0.vapi
