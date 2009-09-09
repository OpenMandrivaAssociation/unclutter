Name:		unclutter
Version:	0.8
Release:	%mkrel 10
Summary:	Hides the mouse cursor when idle
Url:		http://www.google.com/search?q=unclutter
Source:		ftp://ftp.x.org/contrib/utilities/unclutter-8.tar.bz2
License:	Public Domain
Group:		System/X11
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	X11-devel imake

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
%setup -n unclutter


%build
xmkmf
make CDEBUGFLAGS="$RPM_OPT_FLAGS"


%install
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


