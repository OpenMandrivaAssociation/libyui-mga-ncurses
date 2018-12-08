%define major 8
%define libname %mklibname yui %{major}-mga-ncurses
%define develname %mklibname yui-mga-ncurses -d

Summary:	UI abstraction library - Mageia extension ncurses plugin
Name:		libyui-mga-ncurses
Version:	1.0.3
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://github.com/manatools/libyui-mga-ncurses
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(libyui) >= 3.1.2
BuildRequires:	%{_lib}yui-ncurses-devel
BuildRequires:	%{_lib}yui-mga-devel >= 1.0.4
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	texlive
BuildRequires:	graphviz
BuildRequires:	ghostscript
Requires:	libyui
Requires:	libyui-mga
Requires:	libyui-ncurses

%description
%{summary}.

#-----------------------------------------------------------------------

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries
Requires:	libyui
Provides:	%{name} = %{EVRD}
Provides:	libyui%{major}-mga-ncurses = %{EVRD}

%description -n %{libname}
This package contains the library needed to run programs
dynamically linked with libyui-mga-ncurses.

%files -n %{libname}
%{_libdir}/yui/lib*.so.*


#-----------------------------------------------------------------------

%package -n %{develname}
Summary:	%{summary} header files
Group:		Development/Other
Requires:	libyui-devel
Requires:	%{libname} = %{EVRD}
Provides:	yui-mga-ncurses-devel = %{EVRD}


%description -n %{develname}
This package provides headers files for libyui-mga-ncurses development.

%files -n %{develname}
%{_includedir}/yui
%{_libdir}/yui/lib*.so
%{_libdir}/pkgconfig/libyui-mga-ncurses.pc
%{_libdir}/cmake/libyui-mga-ncurses

#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build
./bootstrap.sh
%cmake \
    -DYPREFIX=%{_prefix} \
    -DDOC_DIR=%{_docdir} \
    -DLIB_DIR=%{_lib}    \
    -DENABLE_DEBUG=1     \
    -DCMAKE_BUILD_TYPE=RELWITHDEBINFO \
    -G Ninja

%ninja_build

%install
%ninja_install -C build

find "%{buildroot}" -name "*.la" -delete
