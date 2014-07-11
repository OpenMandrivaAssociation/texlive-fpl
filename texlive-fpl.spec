# revision 15878
# category Package
# catalog-ctan /fonts/fpl
# catalog-date 2007-09-28 22:20:10 +0200
# catalog-license gpl
# catalog-version 1.002
Name:		texlive-fpl
Version:	1.002
Release:	8
Summary:	SC and OsF fonts for URW Palladio L
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/fpl
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fpl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fpl.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fpl.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The FPL Fonts provide a set of SC/OsF fonts for URW Palladio L
which are compatible with respect to metrics with the Palatino
SC/OsF fonts from Adobe. Note that it is not my aim to exactly
reproduce the outlines of the original Adobe fonts. The SC and
OsF in the FPL Fonts were designed with the glyphs from URW
Palladio L as starting point. For some glyphs (e.g. 'o') I got
the best result by scaling and boldening. For others (e.g. 'h')
shifting selected portions of the character gave more
satisfying results. All this was done using the free font
editor FontForge. The kerning data in these fonts comes from
Walter Schmidt's improved Palatino metrics. LaTeX use is
enabled by the mathpazo package, which is part of the psnfss
distribution.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/fpl/fplbij8a.afm
%{_texmfdistdir}/fonts/afm/public/fpl/fplbj8a.afm
%{_texmfdistdir}/fonts/afm/public/fpl/fplrc8a.afm
%{_texmfdistdir}/fonts/afm/public/fpl/fplrij8a.afm
%{_texmfdistdir}/fonts/afm/public/fpl/pplb9d-kern.afm
%{_texmfdistdir}/fonts/afm/public/fpl/pplbi9d-kern.afm
%{_texmfdistdir}/fonts/afm/public/fpl/pplrc9d-kern.afm
%{_texmfdistdir}/fonts/afm/public/fpl/pplri9d-kern.afm
%{_texmfdistdir}/fonts/type1/public/fpl/fplbij8a.pfb
%{_texmfdistdir}/fonts/type1/public/fpl/fplbij8a.pfm
%{_texmfdistdir}/fonts/type1/public/fpl/fplbj8a.pfb
%{_texmfdistdir}/fonts/type1/public/fpl/fplbj8a.pfm
%{_texmfdistdir}/fonts/type1/public/fpl/fplrc8a.pfb
%{_texmfdistdir}/fonts/type1/public/fpl/fplrc8a.pfm
%{_texmfdistdir}/fonts/type1/public/fpl/fplrij8a.pfb
%{_texmfdistdir}/fonts/type1/public/fpl/fplrij8a.pfm
%doc %{_texmfdistdir}/doc/fonts/fpl/COPYING
%doc %{_texmfdistdir}/doc/fonts/fpl/README
#- source
%doc %{_texmfdistdir}/source/fonts/fpl/AddException
%doc %{_texmfdistdir}/source/fonts/fpl/AddGPL
%doc %{_texmfdistdir}/source/fonts/fpl/Makefile
%doc %{_texmfdistdir}/source/fonts/fpl/Palladio-BoldItalicOsF.sfd
%doc %{_texmfdistdir}/source/fonts/fpl/Palladio-BoldOsF.sfd
%doc %{_texmfdistdir}/source/fonts/fpl/Palladio-ItalicOsF.sfd
%doc %{_texmfdistdir}/source/fonts/fpl/Palladio-SC.sfd
%doc %{_texmfdistdir}/source/fonts/fpl/README
%doc %{_texmfdistdir}/source/fonts/fpl/TeXPalladioL-BoldItalicOsF.pe
%doc %{_texmfdistdir}/source/fonts/fpl/TeXPalladioL-BoldOsF.pe
%doc %{_texmfdistdir}/source/fonts/fpl/TeXPalladioL-ItalicOsF.pe
%doc %{_texmfdistdir}/source/fonts/fpl/TeXPalladioL-SC.pe
%doc %{_texmfdistdir}/source/fonts/fpl/URW-OtherSubrs.ps

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.002-2
+ Revision: 752090
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.002-1
+ Revision: 718500
- texlive-fpl
- texlive-fpl
- texlive-fpl
- texlive-fpl

