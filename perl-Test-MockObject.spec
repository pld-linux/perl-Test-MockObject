#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	MockObject
Summary:	Test::MockObject - Perl extension for emulating troublesome interfaces
#Summary(pl):	
Name:		perl-Test-MockObject
Version:	1.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b056d6cc9c287285c1e5b04b04384178
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-UNIVERSAL-can >= 1.00
BuildRequires:	perl-UNIVERSAL-isa >= 0.02
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Warn
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It's a simple program that doesn't use any other modules, and those are easy to
test.  More often, testing a program completely means faking up input to
another module, trying to coax the right output from something you're not
supposed to be testing anyway.

Testing is a lot easier when you can control the entire environment.  With
Test::MockObject, you can get a lot closer.

Test::MockObject allows you to create objects that conform to particular
interfaces with very little code.  You don't have to reimplement the behavior,
just the input and the output.

# %description -l pl
# TODO

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
