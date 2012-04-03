Name: task-gnome
Version: 2012
Release: 2.1
Summary: Metapackage for GNOME desktop environment
Group: Graphical desktop/GNOME
License: GPLv2+
BuildArch: noarch

Requires: %{name}-minimal
# MD 2012_04_02
# anything with suggests is replaceable
# anything with requires adds functionality
# please change if you disagree
Requires: cheese
Requires: eog
Requires: evince
Requires: folks
Requires: gcalctool
Requires: gnome-color-manager
Requires: gnome-disk-utility
Requires: file-roller
Requires: libsocialweb
Requires: rhythmbox
Requires: telepathy-mission-control
Requires: totem
Requires: tracker-applet
Requires: tracker-preferences

#extras
Suggests: empathy
Suggests: epiphany
Suggests: epiphany-extensions
Suggests: gedit
Suggests: gdm
# do ppl still own these
Suggests: gnome-pilot

# games
Suggests: gnome-games

# mono
Suggests: f-spot
Suggests: tomboy

# biz / office / utils
Suggests: brasero
Suggests: caribou
Suggests: caribou-gtk3
Suggests: ekiga
Suggests: evolution
Suggests: evolution-tracker
Suggests: evolution-webcal
Suggests: gnome-contacts
Suggests: gok
Suggests: gucharmap
Suggests: mousetweaks
Suggests: nautilus-filesharing
Suggests: nautilus-sendto-bluetooth
Suggests: nautilus-sendto-evolution
Suggests: orca
Suggests: vino
Suggests: vinagre

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the GNOME.

%package minimal
Summary: Minimal dependencies needed for GNOME desktop 
Group: Graphical desktop/GNOME

Requires: accountsservice
Requires: gnome-applets
Requires: gnome-control-center
Requires: gnome-icon-theme-symbolic
Requires: gnome-power-manager
Requires: gnome-system-monitor
Requires: gnome-terminal
Requires: gnome-themes-standard
Requires: gnome-tweak-tool
Requires: gnome-utils
# to be replaced in 3.4
# gnome-boxes gnome-font-viewer baobab gnome-system-log gnome-search-tool
# gnome-dictionary gnome-screenshot
Requires: libgnomekbd
Requires: libgnomekbd-common
Requires: nautilus
Requires: networkmanager-applet
Requires: yelp
# gnome3 fallback
#Suggests: ???
Requires: gnome-panel
Requires: gobject-introspection
Requires: metacity
#Suggests: mandriva-theme does mdv care?
Suggests: gnome-media
Suggests: preload
Suggests: task-pulseaudio

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal GNOME desktop environment.

%files

%files minimal


