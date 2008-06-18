Name: task-gnome
Version: 2008.1
Release: %mkrel 5
Summary: Metapackage for the GNOME
Group: Graphical desktop/GNOME
License: GPL
Requires: %{name}-minimal
Requires: gedit >= 2.8.0
Requires: gdm >= 2.4.1.3
Requires: gnome-media >= 2.8.0
Requires: gconf-editor >= 2.8.0
Requires: gnome-games >= 2.8.0
Requires: gok
Requires: orca
Requires: rhythmbox
Requires: file-roller
Requires: gnome-pilot
Requires: totem
Requires: epiphany
Requires: epiphany-extensions
Requires: gnome-mag
Requires: gucharmap
Requires: gcalctool
Requires: beagle-gui
Requires: eog >= 2.8.0
Requires: pidgin
Requires: ekiga
Requires: evolution
Requires: evolution-webcal
Requires: beagle-evolution
Requires: nautilus
Requires: nautilus-cd-burner
Requires: nautilus-filesharing
Requires: tomboy
Requires: dasher
Requires: f-spot
Requires: deskbar-applet
Requires: evince
Requires: vino
Requires: vinagre
Suggests: nautilus-sendto-bluetooth
Suggests: nautilus-sendto-evolution
Suggests: brasero
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
Requires: gnome-volume-manager >= 1.5.15
Suggests: bug-buddy >= 2.8.0
Suggests: task-pulseaudio

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


