%include	/usr/lib/rpm/macros.perl
%define	pdir	AI
%define	pnam	jNeural
Summary:	AI::jNeural::arch - The Jet's Neural Architecture base module
Name:		perl-%{pdir}-%{pnam}
Version:	0.52
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildRequires:	flex jneural-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This particular module doesn't actually do anything.  It would be the
place to look for functions that are general to the entire library,
but there really arn't any yet.

# %description -l pl
# szkoda zachodu

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
%{perl_sitearch}/AI/*.pm
%{perl_sitearch}/AI/jNeural
%dir %{perl_sitearch}/auto/AI/jNeural
%{perl_sitearch}/auto/AI/jNeural/*.ix
%{perl_sitearch}/auto/AI/jNeural/*/*.ix
%{perl_sitearch}/auto/AI/jNeural/*/*/*.ix
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
