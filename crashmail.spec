Summary:	A Fidonet *.JAM and MSG tosser
Summary(pl):	Program do rzucania *.JAM i MSG w Fidonecie
Name:		crashmail
Version:	0.62
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.df.lth.se/~billing/crashmail/cm062linux.zip
# Source0-md5:	1626183c0d2ced4a9b01742458405036
URL:		http://http://www.df.lth.se/~billing/crashmail.html
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Fidonet *.JAM and MSG tosser.

%description -l pl
Program do rzucania *.JAM i MSG w Fidonecie.

%prep
%setup -q -n CrashMail

%build
cd src
%{__make} linux

%install
rm -rf $RPM_BUILD_ROOT
install -d	$RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install bin/*	$RPM_BUILD_ROOT%{_bindir}
install man/*	$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
