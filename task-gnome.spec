Name: task-gnome
Version: 2010.1
Release: %mkrel 1
Summary: Metapackage for the GNOME
Group: Graphical desktop/GNOME
License: GPL
Requires: %{name}-minimal
Suggests: gedit >= 2.8.0
Suggests: gdm >= 2.4.1.3
Suggests: gconf-editor >= 2.8.0
Suggests: gnome-games >= 2.8.0
Suggests: rhythmbox
Suggests: file-roller
Suggests: gnome-pilot
Suggests: totem
Suggests: epiphany
Suggests: epiphany-extensions
Suggests: gucharmap
Suggests: gcalctool
Suggests: beagle-gui
Suggests: eog >= 2.8.0
Suggests: empathy
Suggests: ekiga
Suggests: evolution
Suggests: evolution-webcal
Suggests: beagle-evolution
Suggests: nautilus
Suggests: nautilus-filesharing
Suggests: tomboy
Suggests: f-spot
Suggests: deskbar-applet
Suggests: evince
Suggests: vino
Suggests: vinagre
Suggests: gok
Suggests: orca
Suggests: mousetweaks
Suggests: dasher
Suggests: nautilus-sendto-bluetooth
Suggests: nautilus-sendto-evolution
Suggests: brasero
Suggests: cheese
Suggests: gnome-color-manager
# not needed, required by gdm
#Requires: zenity

# the following packages still rest in contrib
#Requires: ggv
#Requires: gpdf
#Requires: gnome-netstatus
#Requires: gtklp
#Requires: gnome-nettool
#Requires: gnome-system-tools

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the GNOME2.

%package minimal
Summary: Minimal dependencies needed for GNOME desktop 
Group: Graphical desktop/GNOME
Obsoletes: gnome2
Provides: gnome2

Requires: gnome-panel >= 2.8.3
Requires: gnome-terminal >= 2.8.2
Requires: nautilus >= 2.8.2
Requires: metacity >= 2.8.13
Requires: yelp >= 2.6.5
Requires: gnome-control-center >= 2.8.2
Requires: gnome-power-manager
Suggests: gnome-media >= 2.8.0
Suggests: bug-buddy >= 2.8.0
Suggests: task-pulseaudio
Suggests: preload
Suggests: readahead

# not needed, required by gnome-panel
#Requires: gnome-applets >= 2.8.0
#Requires: gnome-utils >= 2.8.0

# not needed, required by gnome-session
#Requires: gnome-user-docs >= 2.6.0

#not needed, required by gnome-applets
#Requires: gnome-system-monitor >= 2.8.0

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal GNOME desktop environment.

%files

%files minimal


