Summary:	Utility library for the XFce4 desktop environment
Summary(pl):	Biblioteka narzêdziowa dla ¶rodowiska XFce4
Name:		libxfce4util
Version:	4.0.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	49528f20c76217ef1def60c23cc00564
URL:		http://www.xfce.org/
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	pkgconfig >= 0.9.0
Requires:	glib2 >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Basic utility non-GUI functions for XFce4.

%description -l pl
Podstawowe funkcje narzêdziowe nie zwi±zane z GUI dla XFce4.

%package devel
Summary:	Development files for libxfce4util library
Summary(pl):	Pliki nag³ówkowe biblioteki libxfce4util
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	glib2-devel >= 2.0.0

%description devel
Development files for the libxfce4util library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libxfce4util.

%package static
Summary:	Static libxfce4util library
Summary(pl):	Statyczna biblioteka libxfce4util
Group:		Development/Libriaries
Requires:	%{name}-devel = %{version}

%description static
Static libxfce4util library.

%description static -l pl
Statyczna biblioteka libxfce4util.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_datadir}/xfce4
%dir %{_datadir}/xfce4/i18n
%{_datadir}/xfce4/i18n/nls.alias

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%dir %{_includedir}/xfce4
%{_includedir}/xfce4/libxfce4util
%{_datadir}/xfce4/m4
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
