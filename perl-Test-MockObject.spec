#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Test
%define	pnam	MockObject
Summary:	Test::MockObject - Perl extension for emulating troublesome interfaces
Summary(pl.UTF-8):	Test::MockObject - rozszerzenie Perla do emulacji kłopotliwych interfejsów
Name:		perl-Test-MockObject
Version:	1.09
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3c9c2842d40fa8c389563c227804d7d8
URL:		http://search.cpan.org/dist/Test-MockObject/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Warn
BuildRequires:	perl-UNIVERSAL-can >= 1.11
BuildRequires:	perl-UNIVERSAL-isa >= 0.06
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It's a simple program that doesn't use any other modules, and those
are easy to test. More often, testing a program completely means
faking up input to another module, trying to coax the right output
from something you're not supposed to be testing anyway.

Testing is a lot easier when you can control the entire environment.
With Test::MockObject, you can get a lot closer.

Test::MockObject allows you to create objects that conform to
particular interfaces with very little code. You don't have to
reimplement the behavior, just the input and the output.

%description -l pl.UTF-8
Jest to prosty program nie używający żadnych innych modułów, a te są
łatwe do sprawdzenia. Co więcej, kompletne przetestowanie programu
oznacza fałszowanie wejścia do innego modułu, próbując wyłudzić
prawdziwe wyjście z czegoś, czego nie powinno się testować.

Testowanie jest dużo łatwiejsze, jeśli można sterować całym
środowiskiem. Przy użyciu Test::MockObject można się do tego zbliżyć.

Test::MockObject pozwala tworzyć obiekty zgodne z pewnymi interfejsami
przy użyciu bardzo małej ilości kodu. Nie trzeba reimplementować
zachowania, wystarczy wejście i wyjście.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/*.pm
%{perl_vendorlib}/Test/MockObject
%{_mandir}/man3/*
