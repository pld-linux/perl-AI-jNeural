#
# Conditional build:
# _without_tests - do not perform "make test"
#
%ifarch ppc
%define		_without_tests	1
%endif

%include	/usr/lib/rpm/macros.perl
%define		pdir	AI
%define		pnam	jNeural
Summary:	AI::jNeural::arch - The Jet's Neural Architecture base module
Summary(pl):	AI::jNeural::arch - podstawowy modu³ Jet's Neural Architecture
Name:		perl-AI-jNeural
Version:	0.53
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	flex
BuildRequires:	jneural-devel
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Math-Business-SMA
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This particular module doesn't actually do anything.  It would be the
place to look for functions that are general to the entire library,
but there really aren't any yet.

%description -l pl
Ten modu³ nie robi w³a¶ciwie niczego. Ma byæ miejscem do szukania
funkcji, które s± ogólne dla ca³ej biblioteki, ale takich jeszcze nie
ma.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
find -type f | xargs perl -pi -e 's,/usr/local,/usr,g'
perl Makefile.PL skip_stuff
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_sitearch}/AI
%{perl_sitearch}/AI/*.pm
%{perl_sitearch}/AI/jNeural
%dir %{perl_sitearch}/auto/AI
%dir %{perl_sitearch}/auto/AI/jNeural
# empty autosplit.ix files
#%{perl_sitearch}/auto/AI/jNeural/*.ix
#%{perl_sitearch}/auto/AI/jNeural/*/*.ix
#%{perl_sitearch}/auto/AI/jNeural/*/*/*.ix
%{perl_sitearch}/auto/AI/jNeural/*.bs
%{perl_sitearch}/auto/AI/jNeural/*/*/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/AI/jNeural/*.so
%attr(755,root,root) %{perl_sitearch}/auto/AI/jNeural/*/*/*.so
%dir %{perl_sitearch}/auto/AI/jNeural/arch
%dir %{perl_sitearch}/auto/AI/jNeural/arch/neuron
%dir %{perl_sitearch}/auto/AI/jNeural/nets
%dir %{perl_sitearch}/auto/AI/jNeural/nets/backprop
%dir %{perl_sitearch}/auto/AI/jNeural/nets/kohonen
%dir %{perl_sitearch}/auto/AI/jNeural/utils
%dir %{perl_sitearch}/auto/AI/jNeural/utils/transfer
%{_mandir}/man3/*
