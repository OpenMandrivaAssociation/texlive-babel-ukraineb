# revision 30298
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-babel-ukraineb
Version:	20131013
Release:	11
Summary:	TeXLive babel-ukraineb package
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-ukraineb.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-ukraineb.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-ukraineb.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive babel-ukraineb package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-ukraineb/ukraineb.ldf
%doc %{_texmfdistdir}/doc/generic/babel-ukraineb/ukraineb.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-ukraineb/ukraineb.dtx
%doc %{_texmfdistdir}/source/generic/babel-ukraineb/ukraineb.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
