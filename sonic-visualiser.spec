Name:           sonic-visualiser
Version:        2.0
Release:        2
Summary:        Application for viewing and analysing the contents of music audio files
Group:          Sound
License:        GPLv2+
URL:            https://www.sonicvisualiser.org
Source0:        http://downloads.sourceforge.net/sv1/%{name}-%{version}.tar.gz
Source1:	sonic-visualiser.desktop

BuildRequires:  raptor-devel
BuildRequires:  liblrdf-devel
BuildRequires:  mad-devel
BuildRequires:  id3tag-devel
BuildRequires:  portaudio-devel
BuildRequires:  qt4-devel
BuildRequires:  pkgconfig(vamp)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  bzip2-devel
BuildRequires:  alsa-oss-devel
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  redland-devel
BuildRequires:  rubberband-devel
BuildRequires:  liboggz-devel
BuildRequires:  libfishsound-devel
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(dataquay)

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
# Fix incorrect version string
sed -i.ver "s|1.9'|2.0'|" sonic-visualiser/configure


%build
%configure2_5x
make

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 -p sonic-visualiser/sonic-visualiser \
        %{buildroot}%{_bindir}/
# desktop file and icon
for s in 16 22 24 32 48 64 128; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
    install -m 644 -p sonic-visualiser/icons/sv-${s}x${s}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/sonic-visualiser.png
done
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}


%files
%doc sonic-visualiser/CHANGELOG sonic-visualiser/COPYING sonic-visualiser/README sonic-visualiser/README.OSC
%{_bindir}/sonic-visualiser
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
