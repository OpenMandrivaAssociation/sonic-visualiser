Name:           sonic-visualiser
Version:        1.7.1
Release:        %mkrel 2
Summary:        Application for viewing and analysing the contents of music audio files
Group:          Sound
License:        GPLv2+
URL:            http://www.sonicvisualiser.org
Source0:        http://downloads.sourceforge.net/sv1/%{name}-%{version}.tar.bz2

# patches kindly borrowed from fedora
Source1:        mandriva-sonic-visualiser.desktop
Patch0:         sonic-visualiser-1.5-gcc44.patch
Patch1:         sonic-visualiser-1.5-alsa.patch
# thanks gentoo for this one
Patch2:         sonic-visualiser-1.7.1-liboggz11.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:  raptor-devel
BuildRequires:  liblrdf-devel
BuildRequires:  mad-devel
BuildRequires:  id3tag-devel
BuildRequires:  portaudio-devel
BuildRequires:  qt4-devel
BuildRequires:  vamp-plugin-sdk-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  fftw-devel
BuildRequires:  bzip2-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  jackit-devel
BuildRequires:  pulseaudio-devel
BuildRequires:  redland-devel
BuildRequires:  rubberband-devel
BuildRequires:  liboggz-devel
BuildRequires:  libfishsound-devel
BuildRequires:  liblo-devel

%description
Sonic Visualiser is an application for viewing and analysing the
contents of musiic audio files. The aim of Sonic Visualiser is to
be the first program you reach for when want to study a musical
recording rather than simply listen to it.

As well as a number of features designed to make exploring audio data
as revealing and fun as possible, Sonic Visualiser also has powerful
annotation capabilities to help you to describe what you find, and the
ability to run automated annotation and analysis plugins in the Vamp
analysis plugin format – as well as applying standard audio effects.

%prep
%setup -q
# https://sourceforge.net/tracker/?func=detail&aid=2715387&group_id=162924&atid=825705
%patch0 -p1 -b .gcc44
# https://sourceforge.net/tracker/?func=detail&aid=2715381&group_id=162924&atid=825705
%patch1 -p1 -b .alsa
%patch2 -p1

%build
qmake
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -m 755 -p sv/sonic-visualiser %{buildroot}%{_bindir}/
install -m 644 -p sv/icons/sv-48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/sonic-visualiser.png
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README README.OSC
%{_bindir}/sonic-visualiser
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
