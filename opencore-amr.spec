%define distsuffix plf

%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	Adaptive Multi Rate speech codec
Name:		opencore-amr
Version:	0.1.3
Release:	1
License:	Apache License
Group:		Sound
Url:		http://opencore-amr.sourceforge.net/
Source0:	http://sourceforge.net/projects/opencore-amr/files/opencore-amr/%{name}-%{version}.tar.gz

%description
This library contains an implementation of the 3GPP TS 26.073
specification for the Adaptive Multi Rate (AMR) speech codec. The
implementation is derived from the OpenCORE framework, part of the
Google Android project.

This package is in restricted for patent reasons.

%package -n %{libname}
Group:		System/Libraries
Summary:	Adaptive Multi Rate speech codec

%description -n %{libname}
This library contains an implementation of the 3GPP TS 26.073
specification for the Adaptive Multi Rate (AMR) speech codec. The
implementation is derived from the OpenCORE framework, part of the
Google Android project.

%package -n %{develname}
Group:		Development/C++
Summary:	Adaptive Multi Rate speech codec - development files
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %develname
This library contains an implementation of the 3GPP TS 26.073
specification for the Adaptive Multi Rate (AMR) speech codec. The
implementation is derived from the OpenCORE framework, part of the
Google Android project.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}

%files -n %{libname}
%doc README LICENSE
%{_libdir}/libopencore-amr??.so.%{major}*

%files -n %{develname}
%{_libdir}/libopencore-amr??.so
%{_libdir}/libopencore-amr??.*a
%{_includedir}/opencore-amr??
%{_libdir}/pkgconfig/opencore-amrnb.pc
%{_libdir}/pkgconfig/opencore-amrwb.pc

%changelog
* Sat Jun 16 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.1.3-1plf
- New version 0.1.3

* Fri Aug 19 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 0.1.2-4plf2011.0
- Port from PLF to restricted
- Little spec clean up

* Wed Dec  2 2009 Götz Waschk <goetz@zarb.org> 0.1.2-1plf2010.1
- update file list
- fix build
- new version

* Mon Jul 20 2009 Götz Waschk <goetz@zarb.org> 0.1.1-1.20090620.1plf2010.0
- add docs
- fix build and installation
- git snapshot

* Mon Jul 20 2009 Götz Waschk <goetz@zarb.org> 0.1.1-1plf2010.0
- initial package

