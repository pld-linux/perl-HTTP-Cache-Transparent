#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTTP
%define	pnam	Cache-Transparent
Summary:	HTTP::Cache::Transparent - Cache the result of HTTP GET requests persistently
Summary(pl):	HTTP::Cache::Transparent - trwa³e zapamiêtywanie wyników ¿±dañ HTTP GET
Name:		perl-HTTP-Cache-Transparent
Version:	0.6
Release:	1
# same as perl 5.8.4+
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	49208c9cd61f8f687c5f5031845c5de2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(LWP)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An implementation of HTTP GET that keeps a local cache of fetched
pages to avoid fetching the same data from the server if it hasn't
been updated. The cache is stored on disk and is thus persistent
between invocations.

Uses the HTTP headers If-Modified-Since and ETag to let the server
decide if the version in the cache is up-to-date or not.

The cache is implemented by modifying the LWP::UserAgent class to
seamlessly cache the result of all requests that can be cached.

%description -l pl
Implementacja HTTP GET przechowuj±ca w lokalnej pamiêci podrêcznej
¶ci±gniête strony, aby zapobiec ¶ci±ganiu tych samych danych z
serwera, je¶li nie zosta³y uaktualnione. Pamiêæ podrêczna jest
zachowywana na dysku, wiêc jest trwa³a pomiêdzy wywo³aniami.

Modu³ u¿ywa nag³ówków HTTP If-Modified-Since i ETag, aby umo¿liwiæ
serwerowi zdecydowanie, czy wersja w buforze jest aktualna, czy nie.

Pamiêæ podrêczna jest zaimplementowana poprzez modyfikacjê klasy
LWP::UserAgent, aby w sposób przezroczysty zapamiêtywaæ wyniki
wszystkich ¿±dañ, które mog± byæ zapamiêtane.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
# perhaps HTTP/Cache dir into perl-base?
%dir %{perl_vendorlib}/HTTP/Cache
%{perl_vendorlib}/HTTP/Cache/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
