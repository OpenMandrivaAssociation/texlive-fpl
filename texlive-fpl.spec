%global tl_name fpl
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.003
Release:	%{tl_revision}.1
Summary:	SC and OsF fonts for URW Palladio L
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/fpl
License:	gpl2 lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fpl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fpl.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fpl.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The FPL Fonts provide a set of SC/OsF fonts for URW Palladio L which are
compatible with respect to metrics with the Palatino SC/OsF fonts from
Adobe. Note that it is not my aim to exactly reproduce the outlines of
the original Adobe fonts. The SC and OsF in the FPL Fonts were designed
with the glyphs from URW Palladio L as starting point. For some glyphs
(e.g. 'o') I got the best result by scaling and boldening. For others
(e.g. 'h') shifting selected portions of the character gave more
satisfying results. All this was done using the free font editor
FontForge. The kerning data in these fonts comes from Walter Schmidt's
improved Palatino metrics. LaTeX use is enabled by the mathpazo package,
which is part of the psnfss distribution.

