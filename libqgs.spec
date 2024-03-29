Summary:	The Qt wrapper around the Ghostscript shared library
Summary(pl.UTF-8):	Wrapper Qt do biblioteki współdzielonej Ghostscripta
Name:		libqgs
Version:	1.0
Release:	2
License:	LGPL
Group:		Development/Libraries
Source0:	http://team.pld-linux.org/~djurban/libqgs/%{name}-%{version}.tar.bz2
# Source0-md5:	2db0481540d3d766468ca247e8f3ef4a
URL:		http://team.pld-linux.org/~djurban/libqgs/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ghostscript-devel
BuildRequires:	qt-devel >= 6:3.3.5
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libqgs is a Qt wrapper around the Ghostscript shared library. It makes
it much easier to use Ghostscript in your Qt application. It saves you
from having to care about starting Ghostscript, parsing its output,
and doing weird tricks to receive the rendered pages. This library
features progressive and nonprogressive rendering of pages, operation
on a QImage object, error handling with support for exceptions, access
to Ghostscript stdio/err messages via signals and via buffer (if
enabled), API documentation, and examples of use.

This library is a part of a project sponsored by Google Summer of
Code program, <http://code.google.com/summerofcode.html>.

%description -l pl.UTF-8
libqgs to wrapper do biblioteki współdzielonej Ghostscripta. Ułatwia
korzystanie z Ghostscripta w aplikacjach Qt. Oszczędza konieczność
dbania o uruchamianie Ghostscripta, analizę jego wyjścia i wykonywania
dziwnych sztuczek w celu otrzymania wyrenderowanych stron. Ta
biblioteka umożliwia progresywne i nieprogresywne renderowanie stron,
operowanie na obiektach QImage, obsługę błędów z obsługą wyjątków,
dostęp do komunikatów Ghostscripta poprzez sygnały i bufor (jeśli jest
włączony), zawiera dokumentację API oraz przykłady użycia.

Ta biblioteka jest częścią projektu sponsorowanego przez program
Google Summer of Code - <http://code.google.com/summerofcode.html>.

%package devel
Summary:	Development files for the Qt wrapper around the Ghostscript shared library
Summary(pl.UTF-8):	Pliki programistyczne wrappera Qt do biblioteki współdzielonej Ghostscripta
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for the Qt wrapper
around the Ghostscript shared library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe dla wrappera Qt do biblioteki
współdzielonej Ghostscripta.

%package examples
Summary:	Code with example use of the Qt wrapper around the Ghostscript shared library
Summary(pl.UTF-8):	Przykłady użycia wrappera Qt do biblioteki współdzielonej Ghostscripta
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description examples
This is the package containing the code with example use of the Qt
wrapper around the Ghostscript shared library.

%description examples -l pl.UTF-8
Ten pakiet zawiera kod z przykładami użycia wrappera Qt do biblioteki
współdzielonej Ghostscripta.

%prep
%setup -q

%build
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -f libqgs/examples/*.cpp $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -f libqgs/examples/*.h $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/qgs.h

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}-%{version}
