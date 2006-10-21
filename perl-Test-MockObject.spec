#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	MockObject
Summary:	Test::MockObject - Perl extension for emulating troublesome interfaces
Summary(pl):	Test::MockObject - rozszerzenie Perla do emulacji k³opotliwych interfejsów
Name:		perl-Test-MockObject
Version:	1.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	197af22ac675405199693ed68f0959e1
URL:		http://search.cpan.org/dist/Test-MockObject/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-UNIVERSAL-can >= 1.11
BuildRequires:	perl-UNIVERSAL-isa >= 0.06
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Warn
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

%description -l pl
Jest to prosty program nie u¿ywaj±cy ¿adnych innych modu³ów, a te s±
³atwe do sprawdzenia. Co wiêcej, kompletne przetestowanie programu
oznacza fa³szowanie wej¶cia do innego modu³u, próbuj±c wy³udziæ
prawdziwe wyj¶cie z czego¶, czego nie powinno siê testowaæ.

Testowanie jest du¿o ³atwiejsze, je¶li mo¿na sterowaæ ca³ym
¶rodowiskiem. Przy u¿yciu Test::MockObject mo¿na siê do tego zbli¿yæ.

Test::MockObject pozwala tworzyæ obiekty zgodne z pewnymi interfejsami
przy u¿yciu bardzo ma³ej ilo¶ci kodu. Nie trzeba reimplementowaæ
zachowania, wystarczy wej¶cie i wyj¶cie.

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
