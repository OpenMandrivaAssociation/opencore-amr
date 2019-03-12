%define distsuffix plf

%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	Adaptive Multi Rate speech codec
Name:		opencore-amr
Version:	0.1.5
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
%configure
%make_build

%install
%make_install


%files -n %{libname}
%doc README LICENSE
%{_libdir}/libopencore-amr??.so.%{major}*

%files -n %{develname}
%{_libdir}/libopencore-amr??.so
%{_includedir}/opencore-amr??
%{_libdir}/pkgconfig/opencore-*.pc
