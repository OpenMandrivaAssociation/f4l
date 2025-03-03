%define name	f4l
%define version	0.2.1
%define cvs	20071120
%if %cvs
%define release %mkrel 0.%cvs.3
%else
%define release %mkrel 3
%endif

%define __libtoolize /bin/true

Name: 	 	%{name}
Summary: 	Flash animation editor
Version: 	%{version}
Release: 	%{release}
%if %cvs
Source0:	%{name}-%{cvs}.tar.lzma
%else
Source0:	%{name}-%{version}.tar.gz
%endif
URL:		https://f4l.sourceforge.net/
License:	GPLv2+
Group:		Graphics
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	qt3-devel
BuildRequires:	doxygen
BuildRequires:	imagemagick
Obsoletes:	f4lm

%description
Flash for Linux is an SWF editor, similar to Macromedia Flash.

%prep
%if %cvs
%setup -q -n %{name}
%else
%setup -q
%endif

%build
%configure2_5x --with-qt-dir=%{qt3dir} --with-qt-libraries=%{qt3lib}
perl -pi -e 's,/usr/lib/qt3/lib,%{qt3lib},g' f4lm/Makefile
%make
										
%install
rm -rf %{buildroot}
%makeinstall

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Flash for Linux
Comment=Flash editor
Exec=%{_bindir}/f4lm
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
MimeType=foo/bar;foo2/bar2;
Categories=Qt;Development;GUIDesigner;Graphics;2DGraphics;VectorGraphics;
EOF

#icons
mkdir -p %{buildroot}/%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
convert -size 48x48 f4lm/main_ico.xpm %{buildroot}/%{_iconsdir}/hicolor/48x48/apps/%{name}.png
mkdir -p %{buildroot}/%_iconsdir
convert -size 32x32 f4lm/main_ico.xpm %{buildroot}/%{_iconsdir}/hicolor/32x32/apps/%{name}.png
mkdir -p %{buildroot}/%_miconsdir
convert -size 16x16 f4lm/main_ico.xpm %{buildroot}/%{_iconsdir}/hicolor/16x16/apps/%{name}.png

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_icon_cache hicolor}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_icon_cache hicolor}
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%{_bindir}/f4lm
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

