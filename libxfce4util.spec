Summary: 	Utility library for the XFce4 desktop environment
Name: 		libxfce4util
Version: 	3.90.0
Release: 	0.1
License:	BSD
URL: 		http://www.xfce.org/
Source0: 	http://belnet.dl.sourceforge.net/sourceforge/xfce/%{name}-%{version}.tar.gz
# Source0-md5:	a76051fe04b9bd030fb6b7d2db302273
Group: 		Development/Libraries
Requires:	glib2 >= 2.0.0
BuildRequires: 	glib2-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Basic utility non-GUI functions for XFce4.

%package devel
Summary:	Development files for libxfce4util library
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for the libxfce4util library.

%package static
Summary:	Static libraries for libxfce4util
Group:		Development/Libriaries
Requires:	%{name}-devel = %{version}

%description static
Static libraries for libxfce4util.

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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xfce4/libxfce4util
%{_datadir}/xfce4/i18n/nls.alias
%{_datadir}/xfce4/m4/

%files static
%defattr(644,root,root,755)
%{_libdir}/*a
