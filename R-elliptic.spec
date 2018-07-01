#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-elliptic
Version  : 1.3.7
Release  : 1
URL      : https://cran.r-project.org/src/contrib/elliptic_1.3-7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/elliptic_1.3-7.tar.gz
Summary  : Elliptic Functions
Group    : Development/Tools
License  : GPL-2.0
Requires: R-calibrator
Requires: R-emulator
BuildRequires : R-calibrator
BuildRequires : R-emulator
BuildRequires : clr-R-helpers

%description
A suite of elliptic and related functions including Weierstrass and
 Jacobi forms.  Also includes various tools for manipulating and
 visualizing complex functions.

%prep
%setup -q -c -n elliptic

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530466140

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530466140
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library elliptic
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library elliptic
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library elliptic
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library elliptic|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/elliptic/CITATION
/usr/lib64/R/library/elliptic/DESCRIPTION
/usr/lib64/R/library/elliptic/INDEX
/usr/lib64/R/library/elliptic/Meta/Rd.rds
/usr/lib64/R/library/elliptic/Meta/demo.rds
/usr/lib64/R/library/elliptic/Meta/features.rds
/usr/lib64/R/library/elliptic/Meta/hsearch.rds
/usr/lib64/R/library/elliptic/Meta/links.rds
/usr/lib64/R/library/elliptic/Meta/nsInfo.rds
/usr/lib64/R/library/elliptic/Meta/package.rds
/usr/lib64/R/library/elliptic/Meta/vignette.rds
/usr/lib64/R/library/elliptic/NAMESPACE
/usr/lib64/R/library/elliptic/R/elliptic
/usr/lib64/R/library/elliptic/R/elliptic.rdb
/usr/lib64/R/library/elliptic/R/elliptic.rdx
/usr/lib64/R/library/elliptic/demo/elliptic.R
/usr/lib64/R/library/elliptic/doc/ellipticpaper.R
/usr/lib64/R/library/elliptic/doc/ellipticpaper.Rnw
/usr/lib64/R/library/elliptic/doc/ellipticpaper.pdf
/usr/lib64/R/library/elliptic/doc/index.html
/usr/lib64/R/library/elliptic/doc/residuetheorem.R
/usr/lib64/R/library/elliptic/doc/residuetheorem.Rnw
/usr/lib64/R/library/elliptic/doc/residuetheorem.pdf
/usr/lib64/R/library/elliptic/help/AnIndex
/usr/lib64/R/library/elliptic/help/aliases.rds
/usr/lib64/R/library/elliptic/help/elliptic.rdb
/usr/lib64/R/library/elliptic/help/elliptic.rdx
/usr/lib64/R/library/elliptic/help/paths.rds
/usr/lib64/R/library/elliptic/html/00Index.html
/usr/lib64/R/library/elliptic/html/R.css
