Name:           sonic-visualiser
Version:        1.7.1
Release:        %mkrel 1
Summary:        Application for viewing and analysing the contents of music audio files
Group:          Sound
License:        GPL2
URL:            http://www.sonicvisualiser.org
Source0:        http://downloads.sourceforge.net/sv1/%{name}-%{version}.tar.bz2
Source1:        sonic-visualiser.desktop
Patch0:         sonic-visualiser-gcc44.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires: libsamplerate-devel
BuildRequires: rubberband-devel
BuildRequires: portaudio-devel
BuildRequires: pulseaudio-devel
BuildRequires: vamp-plugin-sdk-devel
BuildRequires: id3tag-devel
BuildRequires: rasqal-devel
BuildRequires: redland-devel

# from upstream's INSTALL
BuildRequires: liblrdf-devel
BuildRequires: liblo-devel
BuildRequires: libfishsound-devel
BuildRequires: liboggz-devel
BuildRequires: mad-devel
BuildRequires: jackit-devel
BuildRequires: bzip2-devel
BuildRequires: libfftw3
BuildRequires: libsamplerate-devel
BuildRequires: sndfile-devel
BuildRequires: qt4-devel

# from upstream's control file
BuildRequires: expat-devel
BuildRequires: libfontconfig1
BuildRequires: libfreetype6-devel
BuildRequires: libice6-devel
BuildRequires: libpcre-devel
BuildRequires: libstdc++6
BuildRequires: libxau6-devel
BuildRequires: libx11_6-devel
BuildRequires: libxcursor1
BuildRequires: libxdmcp6-devel
BuildRequires: libxext6-devel
BuildRequires: libxfixes-devel
BuildRequires: libxrender1-devel
BuildRequires: zlib1-devel
BuildRequires: libalsa-devel
BuildRequires: libcurl-devel

%description
The aim of Sonic Visualiser is to be the first program you reach for when want
to study a musical recording rather than simply listen to it.

%prep
%setup -q
%patch0 -p1

%build
qmake
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -m 755 -p sv/sonic-visualiser $RPM_BUILD_ROOT%{_bindir}/
install -m 644 -p sv/icons/sv-48x48.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/sonic-visualiser.png
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGELOG COPYING README*
%{_bindir}/sonic-visualiser
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
