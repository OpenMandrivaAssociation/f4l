%define name	f4l
%define version	0.2
%define release %mkrel 2

%define __libtoolize /bin/true

Name: 	 	%{name}
Summary: 	Flash animation editor
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://f4l.sourceforge.net/
License:	GPL
Group:		Graphics
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	qt3-devel ImageMagick
Provides:	flash4linux f4l
Obsoletes:	f4lm
#Provides:	f4lm

%description
Flash for Linux is an SWF editor, similar to Macromedia Flash.

%prep
%setup -q

%build
make QTDIR=/usr/lib/qt3
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="Flash for Linux" longtitle="SWF animation editor" section="Multimedia/Graphics"
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 src/cursor/main_ico.xpm $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 src/cursor/main_ico.xpm $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 src/cursor/main_ico.xpm $RPM_BUILD_ROOT/%_miconsdir/%name.png

mkdir -p $RPM_BUILD_ROOT/%_bindir
cp bin/* $RPM_BUILD_ROOT/%_bindir

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
#%doc AUTHORS COPYING ChangeLog README TODO
%{_bindir}/%name
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
