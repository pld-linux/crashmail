Summary:	A Fidonet *.JAM and MSG tosser
Summary(pl.UTF-8):   Program do rzucania *.JAM i MSG w Fidonecie
Name:		crashmail
Version:	0.71
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.df.lth.se/~billing/crashmail/cm071linux.zip
# Source0-md5:	c10de7a0e6f48e7b1cd2cabad8ed8289
URL:		http://www.df.lth.se/~billing/crashmail.html
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Fidonet *.JAM and MSG tosser.

%description -l pl.UTF-8
Program do rzucania *.JAM i MSG w Fidonecie.

%prep
%setup -q

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
