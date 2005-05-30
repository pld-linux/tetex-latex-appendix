
%define short_name appendix

Summary:	Extra control of appendices
Summary(pl):	Wi�ksza kontrola nad formatowaniem dodatk�w
Name:		tetex-latex-%{short_name}
Version:	1.3
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	ftp://ftp.ctan.org/tex-archive/macros/latex/contrib/%{short_name}.zip
# Source0-md5:	171ec47cb9ee78637fe45af39e3a6551
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/appendix/
Requires(post,postun):	/usr/bin/texhash
Requires:	tetex-latex
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

%description
The appendix package provides various ways of formatting the titles of
appendices. Also (sub)appendices environments are provided that can be
used, for example, for per chapter/section appendices.

%description -l pl
Ten pakiet pozwala na wi�ksz� kontrol� nad formatowaniem tytu��w
dodatk�w. Dodatkowo, udost�pnia �rodowiska (pod)dodatk�w co mo�e by�
przydatne na przyk�ad podczas tworzenia dodatk�w dla rozdzia�u/sekcji.

%prep
%setup -q -n %{short_name}

%build
latex %{short_name}.ins

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/{tex,doc}/latex/%{short_name}

install *.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install *.pdf $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/texmf/tex/latex/%{short_name}/*
%doc %{_datadir}/texmf/doc/latex/%{short_name}/*