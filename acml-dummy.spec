Summary:	AMD Core Math Library
Summary(pl.UTF-8):	Podstawowa biblioteka matematyczna AMD (ACML)
Name:		acml-dummy
Version:	2.5.0
Release:	1
License:	GPL
Group:		Libraries
URL:		http://www.developwithamd.com/acml/
Provides:	libacml.so()(64bit)
ExclusiveArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ACML is a set of highly-optimized numerical libraries for use with
64-bit processors made by AMD. This package is meant to provide
dependencies for RPM. Libraries and include files should be obtained
separately from AMD website.

%description -l pl.UTF-8
ACML jest zestawem mocno optymalizowanych bibliotek numerycznych,
przeznaczonych do użycia z 64-bitowymi procesorami firmy AMD. Ten pakiet
dostarcza niezbędnych zależności systemowi RPM. Biblioteki i pliki
nagłówkowe trzeba ściągnąć samemu ze strony internetowej AMD.

%prep
%setup -q -T

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
