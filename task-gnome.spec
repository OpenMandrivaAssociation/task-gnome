Summary:	Metapackage for GNOME desktop environment
Name:		task-gnome
Version:	47.0
Release:	2
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
Recommends: gnome-text-editor
Recommends: gdm
Recommends: gnome-color-manager
Recommends: gnome-disk-utility
# Crashing at package searching, disable for now. Gnome-software works better.
#Recommends: gnome-packagekit
Recommends: gnome-software
Recommends: gnome-terminal-nautilus
Recommends: gnome-tweaks
#Recommends: console
# No need to pull seconds web browser. Main and fully featured is Firefox.
#Recommends: epiphany
#Recommends: gnome-games
Recommends:  aisleriot
Recommends:  gnome-chess
Recommends:  gnome-mahjongg
Recommends:  gnome-nibbles
#Recommends: rhythmbox
#Recommends: lollypop
Recommends:  g4music
# De bloat, totem is a bit old software, and we already provide clapper.
#Recommends: totem
Recommends: loupe
# Empathy is no longer in active development and still require old, dropped webkit 4.0. Lets remove it.
Obsoletes: empathy

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

#Recommends: bijiben
Recommends: gnome-characters
Recommends: gnome-clocks
# This is needed only for devs.
#Recommends: gnome-builder
Recommends: gnome-calendar
Recommends: gnome-dictionary
# broken right now + obsoletes, no longer in development and require dropped webkit 4.0
Obsoletes: gnome-documents
Recommends: foliate
Recommends: gnome-font-viewer
Recommends: gnome-sound-recorder
Recommends: gnome-usage
Recommends: gnome-weather
Recommends: baobab
Recommends: gnome-system-log
# old, no longer needed
#Recommends: gnome-search-tool
Recommends: gnome-commander

Recommends: gucharmap
Recommends: mousetweaks
#Suggests: nautilus-filesharing
Recommends: nautilus-sendto

#Suggests: orca
Recommends: simple-scan
Recommends: shotwell
Recommends: sushi
# Disable for now, too old to keep in task/ISO but still good to install by user.
#Recommends: vino
#Recommends: vinagre
Recommends: polari
#or srain
#Recommends: srain
Recommends: fractal

Recommends: gnome-maps
Recommends: gnome-music
# One year old but still good?
#Recommends: gnome-photos
Recommends: clapper
#Recommends: celluloid

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the GNOME.

%package minimal
Summary:	A very minimal GNOME 3 desktop
Group:		Graphical desktop/GNOME

Requires: adobe-source-code-pro-fonts
Requires: accountsservice
Requires: adwaita-icon-theme
Requires: gnome-desktop
Requires: gnome-backgrounds
Requires: gnome-control-center
Requires: gnome-menus
Requires: gnome-panel
Requires: gnome-power-manager
Requires: gnome-keyring
#Requires: gnome-screenshot
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
Recommends: xdg-desktop-portal-gnome

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
