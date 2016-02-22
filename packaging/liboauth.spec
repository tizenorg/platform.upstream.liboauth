Name:       liboauth
Summary:    OAuth - server to server secure API authentication
Version: 1.0.3
Release:    1
Group:      Social & Content/API
License:    MIT
URL:        http://liboauth.sourceforge.net/
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(openssl)

%description
library implementing the OAuth secure authentication protocol (shared libs)

%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
%description devel
Development files for %{name}

%prep
%setup -q

%build

%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp %{_builddir}/%{name}-%{version}/COPYING.MIT %{buildroot}/usr/share/license/%{name}

%make_install

%post -n liboauth -p /sbin/ldconfig
%post -n liboauth-devel -p /sbin/ldconfig

%postun -n liboauth -p /sbin/ldconfig
%postun -n liboauth-devel -p /sbin/ldconfig

%files
/usr/share/license/%{name}
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*.h
%{_datadir}/man/*

