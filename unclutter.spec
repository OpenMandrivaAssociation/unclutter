Name:		unclutter
Version:	0.8
Release:	13
Summary:	Hides the mouse cursor when idle
Url:		http://www.google.com/search?q=unclutter
Source:		ftp://ftp.x.org/contrib/utilities/unclutter-8.tar.bz2
Patch0:		unclutter-link.patch
License:	Public Domain
Group:		System/X11
BuildRequires:	pkgconfig(x11)
BuildRequires:	imake

%description
Unclutter is a program which runs permanently in the background of an X11
session.  It checks on the X11 pointer (cursor) position every few seconds, and
when it finds it has not moved (and no buttons are pressed on the mouse, and
the cursor is not in the root window) it creates a small sub-window as a child
of the window the cursor is in.  The new window installs a cursor of size 1x1
but a mask of all 0, ie an invisible cursor.  This allows you to see all the
text in an xterm or xedit, for example.  The human factors crowd would agree it
should make things less distracting.


%prep
%setup -qn unclutter
%patch0 -p0

%build
xmkmf
make CDEBUGFLAGS="%optflags" EXTRA_LDOPTIONS="%ldflags"

%install
rm -fr %buildroot
mkdir -p 		$RPM_BUILD_ROOT/%_bindir
install -s unclutter	$RPM_BUILD_ROOT/%_bindir/unclutter

mkdir -p 		$RPM_BUILD_ROOT/%_mandir/man6
install unclutter.man 	$RPM_BUILD_ROOT/%_mandir/man6/unclutter.6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(-,root,root) %doc README
%attr(755,root,root) %_bindir/unclutter
%attr(644,root,root) %_mandir/man6/unclutter.6*


%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 0.8-11mdv2011.0
+ Revision: 634751
- drop unneeded linking library

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 0.8-10mdv2010.0
+ Revision: 434542
- rebuild
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.8-8mdv2009.0
+ Revision: 255142
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 6mdv2008.1-current
+ Revision: 140924
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Dec 05 2006 Michael Scherer <misc@mandriva.org> 0.8-6mdv2007.0
+ Revision: 91340
- adjust group
- adjust BuildRequires
- use mkrel
- Import unclutter

