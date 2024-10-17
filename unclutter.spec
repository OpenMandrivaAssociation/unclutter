Name:		unclutter
Version:	1.09
Release:	1
Summary:	Hides the mouse cursor when idle
Url:		https://www.google.com/search?q=unclutter
Source0:	http://downloads.sourceforge.net/project/unclutter/unclutter/source_%{version}/%{name}-%{version}.tar.gz
Patch0:		unclutter-link.patch
License:	Public Domain
Group:		System/X11
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	imake gccmakedep

%description
Unclutter runs in the background of an X11 session and after a
specified period of inactivity hides the cursor from display. When
the cursor is moved its display is restored. Users may specify
specific windows to be ignored by unclutter.

%prep
%setup -q
%autopatch -p1
sed -i -e 's,^BINDIR.*,BINDIR=%{_bindir},;s,^MANDIR.*,MANDIR=%{_mandir},' Imakefile
xmkmf -a

%build
%make CDEBUGFLAGS="%optflags" EXTRA_LDOPTIONS="%ldflags"

%install
%makeinstall_std install.man MANDIR=%{_mandir}/man1

%files
%attr(-,root,root) %doc README
%attr(755,root,root) %_bindir/unclutter
%attr(644,root,root) %_mandir/man1/unclutter.1*
