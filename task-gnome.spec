Summary:	Metapackage for GNOME desktop environment
Name:		task-gnome
Version:	41.0
Release:	1
Group:		Graphical desktop/GNOME
License:	GPLv2+
BuildArch:	noarch

# task-gnome dependencies:
# for a "Fully featured GNOME 3 desktop".

Requires:	%{name}-minimal
Obsoletes:	gnome-utils

Recommends: cheese
Recommends: eog
Recommends: evince
Recommends: file-roller
Recommends: gnome-calculator
Recommends: gedit
Recommends: gdm
Recommends: gnome-color-manager
Recommends: gnome-disk-utility
Recommends: gnome-packagekit
Recommends: gnome-software
Recommends: gnome-terminal-nautilus
Recommends: gnome-tweaks

Recommends: empathy
Recommends: epiphany
Recommends: gnome-games
Recommends: rhythmbox
Recommends: lollypop
Recommends: totem

# biz / office / utils
Recommends: brasero
Recommends: caribou
Recommends: caribou-gtk3
Recommends: ekiga
Recommends: evolution
# Too much dependency to install. Leave it disabled, let users choose.
#Recommends: gnome-boxes
Recommends: gnome-contacts
Recommends: gparted
Recommends: gthumb

# DONT KNOW...
#Recommends: gimp
#Recommends: inkscape
#Recommedns: geary
#Recommends: peak

#NOT PACKED YET
#Recommends: gnome-epub-thumbnailer
#Recommends: gnome-multi-writer
#Recommends: gnome-todo

Recommends: bijiben
Recommends: gnome-characters
Recommends: gnome-clocks
# This is needed only for devs.
#Recommends: gnome-builder
Recommends: gnome-calendar
Recommends: gnome-dictionary
Recommends: gnome-documents
Recommends: gnome-font-viewer
Recommends: gnome-sound-recorder
Recommends: gnome-usage
Recommends: gnome-weather
Recommends: baobab
Recommends: gnome-system-log
Recommends: gnome-search-tool
Recommends: gnome-commander

Recommends: gucharmap
Recommends: mousetweaks
#Suggests: nautilus-filesharing
Recommends: nautilus-sendto

#Suggests: orca
Recommends: simple-scan
Recommends: shotwell
Recommends: sushi
Recommends: vino
Recommends: vinagre
Recommends: polari
#or srain
#Recommends: srain
Recommends: fractal

Recommends: gnome-maps
# Broken fow now. Tracker issue. Let's use rhytmbox and lollypop
#Recommends: gnome-music
Recommends: gnome-photos

Recommends: celluloid

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the GNOME.

%package minimal
Summary:	A very minimal GNOME 3 desktop
Group:		Graphical desktop/GNOME

Requires: accountsservice
Requires: adwaita-icon-theme
Requires: gnome-desktop
Requires: gnome-backgrounds
Requires: gnome-control-center
Requires: gnome-menus
Requires: gnome-panel
Requires: gnome-power-manager
Requires: gnome-keyring
Requires: gnome-screenshot
Requires: gnome-shell
Requires: gnome-system-monitor
Requires: gnome-terminal
Requires: gnome-themes-standard
Requires: nautilus
Requires: networkmanager
Requires: task-pulseaudio
Requires: yelp
Recommends: task-x11
Recommends: task-pulseaudio

# For dnfdragora
Recommends: libyui-gtk
Recommends: libyui-mga-gtk


# ENABLE AFTER TEST
# classic session:
#Requires: gnome-classic-session

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal GNOME desktop environment.

%files

%files minimal
