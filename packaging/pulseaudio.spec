%define pulseversion 2.0

Name:       pulseaudio
Summary:    Improved Linux sound server
Version:    2.0
Release:    0
Group:      Multimedia/PulseAudio
License:    LGPLv2+
URL:        http://pulseaudio.org
Source0:    http://127.0.0.1/pulseaudio-2.0.tar.gz
Patch0: 0001-build-sys-install-files-for-a-module-development.patch
Patch1: 0002-jack-detection-fix-for-wired-headset.patch
Patch2: 0003-volume-ramp-additions-to-the-low-level-infra.patch
Patch3: 0004-volume-ramp-adding-volume-ramping-to-sink-input.patch
Patch4: 0005-volume-ramp-add-volume-ramping-to-sink.patch
Patch5: 0006-make-pa_thread_mq_done-safe-for-subsequent-calls.patch
Patch6: 0007-bluetooth-Set-initial-profile-priority-based-on-prof.patch
Patch7: 0008-bluetooth-Don-t-force-any-profile-on-discovery-modul.patch
Patch8: 0009-packaging-added-spec.in-and-pulseaudio.service.patch
Patch9: 0010-configuration-IVI-additions-to-default-config-files.patch
Patch10: 0011-packaging-let-the-basic-package-pull-in-the-config.patch
Patch11: 0012-scripts-added-OBS-exporter-script.patch
Patch12: 0013-packaging-updated-build-dependencies-to-be-in-line-w.patch
Patch13: 0014-packaging-put-systemd-service-units-under-_libdir.patch
Patch14: 0015-packaging-module-devel-requires-version-exact-libs-d.patch
Patch15: 0016-packaging-make-separate-package-for-module-augment-p.patch
Requires:   udev
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: pulseaudio-config
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  libatomic_ops-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  json-c-devel
BuildRequires:  m4
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libtool
BuildRequires:  intltool
BuildRequires:  fdupes


%description
PulseAudio is a sound server for Linux and other Unix like operating
systems. It is intended to be an improved drop-in replacement for the
Enlightened Sound Daemon (ESOUND).

%package libs
Summary:    PulseAudio client libraries
Group:      Multimedia/PulseAudio
Requires:   %{name} = %{version}-%{release}

%description libs
Client libraries used by applications that access a PulseAudio sound server
via PulseAudio's native interface.


%package libs-devel
Summary:    PulseAudio client development headers and libraries
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description libs-devel
Headers and libraries for developing applications that access a PulseAudio
sound server via PulseAudio's native interface


%package utils
Summary:    Command line tools for the PulseAudio sound server
Group:      Multimedia/PulseAudio
Requires:   %{name} = %{version}-%{release}

%description utils
These tools provide command line access to various features of the
PulseAudio sound server. Included tools are:
pabrowse - Browse available PulseAudio servers on the local network.
paplay - Playback a WAV file via a PulseAudio sink.
pacat - Cat raw audio data to a PulseAudio sink.
parec - Cat raw audio data from a PulseAudio source.
pacmd - Connect to PulseAudio's built-in command line control interface.
pactl - Send a control command to a PulseAudio server.
padsp - /dev/dsp wrapper to transparently support OSS applications.
pax11publish - Store/retrieve PulseAudio default server/sink/source
settings in the X11 root window.


%package module-bluetooth
Summary:    Bluetooth module for PulseAudio sound server
Group:      Multimedia/PulseAudio
Requires:   %{name} = %{version}-%{release}

%description module-bluetooth
This module enables PulseAudio to work with bluetooth devices, like headset
or audio gatewa

%package module-devel
Summary:        Headers and libraries for PulseAudio module development
License:        LGPLv2+
Group:          Development/Libraries
Requires:       %{name}-libs-devel = %{version}-%{release}

%package config
Summary: Default configuration for PulseAudio.
Group: System Environment/Configuration

%description config
Default configuration for PulseAudio.

%description module-devel
Headers and libraries for developing pulseaudio modules

#%package module-zeroconf
#Summary: PA module-zeroconf
#Group:   Multimedia/PulseAudio
#
#%description module-zeroconf
#PA module-zeroconf.

%package module-raop
Summary: PA module-raop
Group:   Multimedia/PulseAudio

%description module-raop
PA module-raop.

%package module-filter
Summary: PA module-filter
Group:   Multimedia/PulseAudio

%description module-filter
PA module-filter.

%package module-combine-sink
Summary: PA module-combine-sink
Group:   Multimedia/PulseAudio

%description module-combine-sink
PA module-combine-sink.

%package module-augment-properties
Summary: PA module-augment-properties
Group:   Multimedia/PulseAudio

%description module-augment-properties
PA module-augment-properties.

%package module-dbus-protocol
Summary: PA module-dbus-protocol
Group:   Multimedia/PulseAudio

%description module-dbus-protocol
PA module-dbus-protocol.

%package module-null-source
Summary: PA module-null-source
Group:   Multimedia/PulseAudio

%description module-null-source
PA module-null-source.

%package module-switch-on-connect
Summary: PA module-swich-on-connect
Group:   Multimedia/PulseAudio

%description module-switch-on-connect
PA module-swich-on-connect.

%package localization
Summary:    PA localization files.
Group:      Multimedia/PulseAudio
Requires:   %{name} = %{version}-%{release}

%description localization
PA localization files.

%package vala-bindings
Summary:    PA Vala bindings.
Group:      Multimedia/PulseAudio
Requires:   %{name} = %{version}-%{release}

%description vala-bindings
PA Vala bindings.


%prep
%setup -q -n pulseaudio-2.0
echo "%{version}" > .tarball-version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
./bootstrap.sh

%build
CPUS="`cat /proc/cpuinfo  | grep ^processor | wc -l`"
JOBS="-j$(($CPUS + 1))"

unset LD_AS_NEEDED
export LDFLAGS+="-Wl,--no-as-needed"
%configure --disable-static --enable-alsa --disable-ipv6 --disable-oss-output --disable-oss-wrapper --enable-bluez --disable-x11 --disable-hal --disable-hal-compat --disable-lirc --disable-avahi --disable-jack --without-fftw --disable-xen
make $JOBS

%install
rm -rf %{buildroot}
%make_install

install -d  %{buildroot}/%{_libdir}/systemd/system
install -m 644 pulseaudio.service %{buildroot}/%{_libdir}/systemd/system/pulseaudio.service
mkdir -p  %{buildroot}/%{_libdir}/systemd/system/multi-user.target.wants
ln -s  ../pulseaudio.service  %{buildroot}/%{_libdir}/systemd/system/multi-user.target.wants/pulseaudio.service

rm -rf  %{buildroot}/etc/xdg/autostart/pulseaudio-kde.desktop
rm -rf  %{buildroot}/usr/bin/start-pulseaudio-kde
rm -rf %{buildroot}/%{_libdir}/pulse-%{pulseversion}/modules/module-device-manager.so

%find_lang pulseaudio
fdupes  %{buildroot}/%{_datadir}
fdupes  %{buildroot}/%{_includedir}

# get rid of *.la files
rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_libdir}/pulseaudio/*.la

# put the default configuration file in place
install -m 644 src/default.pa %{buildroot}/%{_sysconfdir}/pulse


%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig


%post module-bluetooth -p /sbin/ldconfig
%postun module-bluetooth -p /sbin/ldconfig


%docs_package

%lang_package


%files
%defattr(-,root,root,-)
%doc LICENSE GPL LGPL
%dir %{_sysconfdir}/pulse/
%{_bindir}/esdcompat
%{_bindir}/pulseaudio
%dir %{_libexecdir}/pulse
%{_libexecdir}/pulse/*
%{_libdir}/libpulsecore-%{pulseversion}.so
%{_libdir}/libpulse-mainloop-glib.so.*
/lib/udev/rules.d/90-pulseaudio.rules
%{_datadir}/pulseaudio/alsa-mixer/paths/*
%{_datadir}/pulseaudio/alsa-mixer/profile-sets/*
%{_bindir}/pamon
/etc/dbus-1/system.d/pulseaudio-system.conf
# cmake stuff
%{_libdir}/cmake/PulseAudio/PulseAudioConfig.cmake
%{_libdir}/cmake/PulseAudio/PulseAudioConfigVersion.cmake
# list all modules
%{_libdir}/pulse-%{pulseversion}/modules/libalsa-util.so
%{_libdir}/pulse-%{pulseversion}/modules/libcli.so
%{_libdir}/pulse-%{pulseversion}/modules/libprotocol-cli.so
%{_libdir}/pulse-%{pulseversion}/modules/libprotocol-http.so
%{_libdir}/pulse-%{pulseversion}/modules/libprotocol-native.so
%{_libdir}/pulse-%{pulseversion}/modules/libprotocol-simple.so
%{_libdir}/pulse-%{pulseversion}/modules/librtp.so
%{_libdir}/pulse-%{pulseversion}/modules/module-alsa-sink.so
%{_libdir}/pulse-%{pulseversion}/modules/module-alsa-source.so
%{_libdir}/pulse-%{pulseversion}/modules/module-always-sink.so
%{_libdir}/pulse-%{pulseversion}/modules/module-console-kit.so
%{_libdir}/pulse-%{pulseversion}/modules/module-device-restore.so
%{_libdir}/pulse-%{pulseversion}/modules/module-stream-restore.so
%{_libdir}/pulse-%{pulseversion}/modules/module-cli-protocol-tcp.so
%{_libdir}/pulse-%{pulseversion}/modules/module-cli-protocol-unix.so
%{_libdir}/pulse-%{pulseversion}/modules/module-cli.so
%{_libdir}/pulse-%{pulseversion}/modules/module-combine.so
%{_libdir}/pulse-%{pulseversion}/modules/module-default-device-restore.so
%{_libdir}/pulse-%{pulseversion}/modules/module-detect.so
%{_libdir}/pulse-%{pulseversion}/modules/module-esound-sink.so
%{_libdir}/pulse-%{pulseversion}/modules/module-http-protocol-tcp.so
%{_libdir}/pulse-%{pulseversion}/modules/module-http-protocol-unix.so
%{_libdir}/pulse-%{pulseversion}/modules/module-intended-roles.so
%{_libdir}/pulse-%{pulseversion}/modules/module-ladspa-sink.so
%{_libdir}/pulse-%{pulseversion}/modules/module-match.so
%{_libdir}/pulse-%{pulseversion}/modules/module-mmkbd-evdev.so
%{_libdir}/pulse-%{pulseversion}/modules/module-native-protocol-fd.so
%{_libdir}/pulse-%{pulseversion}/modules/module-native-protocol-tcp.so
%{_libdir}/pulse-%{pulseversion}/modules/module-native-protocol-unix.so
%{_libdir}/pulse-%{pulseversion}/modules/module-null-sink.so
%{_libdir}/pulse-%{pulseversion}/modules/module-pipe-sink.so
%{_libdir}/pulse-%{pulseversion}/modules/module-pipe-source.so
%{_libdir}/pulse-%{pulseversion}/modules/module-position-event-sounds.so
%{_libdir}/pulse-%{pulseversion}/modules/module-remap-sink.so
%{_libdir}/pulse-%{pulseversion}/modules/module-rescue-streams.so
%{_libdir}/pulse-%{pulseversion}/modules/module-rtp-recv.so
%{_libdir}/pulse-%{pulseversion}/modules/module-rtp-send.so
%{_libdir}/pulse-%{pulseversion}/modules/module-simple-protocol-tcp.so
%{_libdir}/pulse-%{pulseversion}/modules/module-simple-protocol-unix.so
%{_libdir}/pulse-%{pulseversion}/modules/module-sine.so
%{_libdir}/pulse-%{pulseversion}/modules/module-tunnel-sink.so
%{_libdir}/pulse-%{pulseversion}/modules/module-tunnel-source.so
%{_libdir}/pulse-%{pulseversion}/modules/module-suspend-on-idle.so
%{_libdir}/pulse-%{pulseversion}/modules/module-volume-restore.so
%{_libdir}/pulse-%{pulseversion}/modules/module-alsa-card.so
%{_libdir}/pulse-%{pulseversion}/modules/module-card-restore.so
%{_libdir}/pulse-%{pulseversion}/modules/module-sine-source.so
%{_libdir}/pulse-%{pulseversion}/modules/module-loopback.so
%{_libdir}/pulse-%{pulseversion}/modules/module-rygel-media-server.so
%{_libdir}/pulse-%{pulseversion}/modules/module-echo-cancel.so
%{_libdir}/pulse-%{pulseversion}/modules/module-virtual-sink.so
%{_libdir}/pulse-%{pulseversion}/modules/module-virtual-source.so
%{_libdir}/pulse-%{pulseversion}/modules/libprotocol-esound.so
%{_libdir}/pulse-%{pulseversion}/modules/module-esound-compat-spawnfd.so
%{_libdir}/pulse-%{pulseversion}/modules/module-esound-compat-spawnpid.so
%{_libdir}/pulse-%{pulseversion}/modules/module-esound-protocol-tcp.so
%{_libdir}/pulse-%{pulseversion}/modules/module-esound-protocol-unix.so
%{_libdir}/pulse-%{pulseversion}/modules/module-gconf.so
%{_libdir}/pulse-%{pulseversion}/modules/module-udev-detect.so
%{_libdir}/pulse-%{pulseversion}/modules/module-role-cork.so
%{_libdir}/pulse-%{pulseversion}/modules/module-switch-on-port-available.so
%{_libdir}/pulse-%{pulseversion}/modules/module-virtual-surround-sink.so
%{_libdir}/systemd/system/pulseaudio.service
%{_libdir}/systemd/system/multi-user.target.wants/pulseaudio.service

%files libs
%defattr(-,root,root,-)
%{_libdir}/libpulse.so.*
%{_libdir}/libpulse-simple.so.*
%{_libdir}/pulseaudio/libpulsecommon-*.so

%files libs-devel
%defattr(-,root,root,-)
%{_includedir}/pulse/*
%{_libdir}/libpulse.so
%{_libdir}/libpulse-simple.so
%{_libdir}/pkgconfig/libpulse-simple.pc
%{_libdir}/pkgconfig/libpulse.pc
%{_datadir}/vala/vapi/libpulse.vapi
%{_libdir}/pkgconfig/libpulse-mainloop-glib.pc
%{_libdir}/libpulse-mainloop-glib.so

%files utils
%defattr(-,root,root,-)
%doc %{_mandir}/man1/*
%doc %{_mandir}/man5/*
%{_bindir}/pacat
%{_bindir}/pacmd
%{_bindir}/pactl
%{_bindir}/paplay
%{_bindir}/parec
%{_bindir}/pamon
%{_bindir}/parecord
%{_bindir}/pasuspender

%files module-bluetooth
%defattr(-,root,root,-)
%{_libdir}/pulse-%{pulseversion}/modules/module-bluetooth-proximity.so
%{_libdir}/pulse-%{pulseversion}/modules/module-bluetooth-device.so
%{_libdir}/pulse-%{pulseversion}/modules/module-bluetooth-discover.so
%{_libdir}/pulse-%{pulseversion}/modules/libbluetooth-ipc.so
%{_libdir}/pulse-%{pulseversion}/modules/libbluetooth-sbc.so
%{_libdir}/pulse-%{pulseversion}/modules/libbluetooth-util.so

#%files module-zeroconf
#%defattr(-,root,root,-)
#%{_libdir}/pulse-%{pulseversion}/modules/libavahi-wrap.so
#%{_libdir}/pulse-%{pulseversion}/modules/module-zeroconf*.so

%files module-raop
%defattr(-,root,root,-)
%{_libdir}/pulse-%{pulseversion}/modules/libraop.so
%{_libdir}/pulse-%{pulseversion}/modules/module-raop*.so

%files module-filter
%defattr(-,root,root,-)
%{_libdir}/pulse-%{pulseversion}/modules/module-filter-*.so

%files module-combine-sink
%defattr(-,root,root,-)
%{_libdir}/pulse-%{pulseversion}/modules/module-combine-sink.so

%files module-augment-properties
%defattr(-,root,root,-)
%{_libdir}/pulse-%{pulseversion}/modules/module-augment-properties.so

%files module-dbus-protocol
%defattr(-,root,root,-)
%{_libdir}/pulse-%{pulseversion}/modules/module-dbus-protocol.so

%files module-null-source
%defattr(-,root,root,-)
%{_libdir}/pulse-%{pulseversion}/modules/module-null-source.so

%files module-switch-on-connect
%defattr(-,root,root,-)
%{_libdir}/pulse-%{pulseversion}/modules/module-switch-on-connect.so

%files config
%defattr(-,root,root,-)
%{_sysconfdir}/pulse/default.pa
%{_sysconfdir}/pulse/client.conf
%{_sysconfdir}/pulse/default.pa
%{_sysconfdir}/pulse/system.pa
%{_sysconfdir}/pulse/daemon.conf

%files module-devel
%defattr(-,root,root)
%{_includedir}/pulsecore
%{_libdir}/pkgconfig/pulseaudio-module-devel.pc

%files localization
%defattr(-,root,root,-)
%{_datadir}/locale/*/LC_MESSAGES/pulseaudio.mo

%files vala-bindings
%defattr(-,root,root,-)
%{_datadir}/vala/vapi/*
