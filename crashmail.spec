Summary:	A Fidonet *.JAM and MSG tosser
Name:		crashmail
Version:	0.62
Release:	1
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
License:	GPL
Source0:	http://www.df.lth.se/~billing/crashmail/cm062linux.zip
URL:		http://http://www.df.lth.se/~billing/crashmail.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Fidonet *.JAM and MSG tosser

%prep
rm -rf CrashMail
unzip -qo %{SOURCE0}
%setup -q -D -T -n CrashMail

%build
cd src
%{__make} linux

%install
rm -rf $RPM_BUILD_ROOT

install -d	$RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install bin/*	$RPM_BUILD_ROOT%{_bindir}
install man/*	$RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
