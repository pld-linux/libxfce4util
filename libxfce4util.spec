
%define		_snap 20040806

Summary:	Utility library for the XFce desktop environment
Summary(pl):	Biblioteka narzêdziowa dla ¶rodowiska XFce
Name:		libxfce4util
Version:	4.2.0
Release:	0.%{_snap}.1
License:	BSD
Group:		Libraries
Source0:	http://ep09.pld-linux.org/~havner/xfce4/%{name}-%{_snap}.tar.bz2
# Source0-md5:	2853200ba40791fea871e5f129fcddd5
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.9.0
Requires:	glib2 >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Basic utility non-GUI functions for XFce.

%description -l pl
Podstawowe funkcje narzêdziowe nie zwi±zane z GUI dla XFce.

%package devel
Summary:	Development files for libxfce4util library
Summary(pl):	Pliki nag³ówkowe biblioteki libxfce4util
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0.0

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
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
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

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
