Summary:	Semi-portable access to hardware-provided atomic memory update operations
Name:		libatomic_ops
Version:	7.4.2
Release:	1
License:	MIT-like (libatomic_ops), GPL v2+ (libatomic_ops_gpl)
Group:		Development/Libraries
Source0:	https://github.com/ivmai/libatomic_ops/archive/%{name}-7_4_2.tar.gz
# Source0-md5:	9c7f41e98cbf4b9dfa54392bc5d9ed65
Patch0:		%{name}-libadd.patch
URL:		https://github.com/ivmai/libatomic_ops
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides semi-portable access to hardware-provided atomic
memory update operations on a number architectures.

%package devel
Summary:	Developmet files for libatomic_ops library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Developmet files for libatomic_ops library.

%prep
%setup -qn libatomic_ops-libatomic_ops-7_4_2
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-static    \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/%{name}

%check
%{__make} check

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS doc/{LICENSING.txt,README.txt,README_malloc.txt,README_stack.txt}
%attr(755,root,root) %ghost %{_libdir}/libatomic_ops.so.1
%attr(755,root,root) %ghost %{_libdir}/libatomic_ops_gpl.so.1
%attr(755,root,root) %{_libdir}/libatomic_ops.so.*.*.*
%attr(755,root,root) %{_libdir}/libatomic_ops_gpl.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libatomic_ops.so
%{_libdir}/libatomic_ops_gpl.so
%{_includedir}/atomic_ops*.h
%{_includedir}/atomic_ops
%{_pkgconfigdir}/atomic_ops.pc

