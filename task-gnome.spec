Summary:	Metapackage for GNOME desktop environment
Name:		task-gnome
Version:	2013
Release:	1
Group:		Graphical desktop/GNOME
License:	GPLv2+
BuildArch:	noarch

Requires: %{name}-minimal
Obsoletes: gnome-utils
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
#Requires: rhythmbox
Requires: telepathy-mission-control
Requires: totem
Requires: tracker

#extras
Suggests: empathy
Suggests: epiphany
Suggests: epiphany-extensions
Suggests: gedit
Requires: gdm
# do ppl still own these
Suggests: gnome-pilot

# games
Suggests: gnome-games

# biz / office / utils
Suggests: brasero
Suggests: caribou
Suggests: caribou-gtk3
Suggests: ekiga
Suggests: evolution
Suggests: evolution-webcal
#Suggests: gnome-boxes
Requires: gnome-contacts
Requires: gnome-dictionary
Requires: gnome-documents
Requires: gnome-font-viewer
Requires: gnome-online-accounts
Suggests: gok
Suggests: gucharmap
Suggests: mousetweaks
Suggests: nautilus-filesharing
Suggests: nautilus-sendto-bluetooth
Suggests: nautilus-sendto-evolution
Suggests: orca
Suggests: simple-scan
Suggests: shotwell
Requires: sushi
Suggests: vino
Suggests: vinagre

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the GNOME.

%package minimal
Summary: Minimal dependencies needed for GNOME desktop 
Group: Graphical desktop/GNOME

Requires: accountsservice
Requires: baobab
Requires: gnome-applets
Requires: gnome-control-center
Requires: gnome-icon-theme-symbolic
Requires: gnome-keyring
Requires: gnome-power-manager
Requires: gnome-system-monitor
Requires: gnome-terminal
Requires: gnome-themes-standard
Requires: gnome-tweak-tool
Requires: gnome-backgrounds
Requires: gnome-system-log
Requires: gnome-search-tool
Requires: gnome-screenshot
Requires: libgnomekbd-common
Requires: libnotify
Requires: nautilus
Requires: networkmanager-applet
Requires: notification-daemon
Requires: packagekit-gtk3-module
Requires: task-pulseaudio
Requires: task-x11
Requires: yelp
# gnome3 fallback
Requires: gnome-panel
Requires: gobject-introspection
Requires: metacity
#Suggests: mandriva-theme does mdv care?
Suggests: gnome-media
Suggests: gnome-packagekit
Suggests: preload

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal GNOME desktop environment.

%files

%files minimal
