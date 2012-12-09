Summary: Metapackage for GNOME desktop environment
Name: task-gnome
Version: 2012
Release: 3.6.1
Group: Graphical desktop/GNOME
License: GPLv2+
BuildArch: noarch

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
Requires: tracker-applet
Requires: tracker-preferences

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
Suggests: evolution-tracker
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



%changelog
* Wed May 09 2012 Matthew Dawkins <mattydaw@mandriva.org> 2012-3.2
+ Revision: 797810
- added req task-x11
- rebuild
- added reqs for missing pkg
- gnome-online-accounts gnome-keyring
- task-pulseaudio libnotify
- notification-daemon packagekit-gtk3-module
- added suggests for gnome-packagekit

* Sun May 06 2012 Matthew Dawkins <mattydaw@mandriva.org> 2012-3.1
+ Revision: 797170
- obsolete gnome-utils

* Sun May 06 2012 Matthew Dawkins <mattydaw@mandriva.org> 2012-3
+ Revision: 796938
- rebuild for gnome 3.4

* Tue Apr 03 2012 Matthew Dawkins <mattydaw@mandriva.org> 2012-2.1
+ Revision: 789020
+ rebuild (emptylog)

* Tue Apr 03 2012 Matthew Dawkins <mattydaw@mandriva.org> 2012-2
+ Revision: 788915
- rebuild
- added another missing dep
- moved gir pkg deps to gnome-shell

* Mon Apr 02 2012 Matthew Dawkins <mattydaw@mandriva.org> 2012-1
+ Revision: 788890
- added reqs for typelib pkgs
- update for gnome3
- first attempt

* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 2010.1-6
+ Revision: 670665
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2010.1-5mdv2011.0
+ Revision: 607977
- rebuild

* Fri May 07 2010 Frederic Crozat <fcrozat@mandriva.com> 2010.1-4mdv2010.1
+ Revision: 543319
- Move some requirements from gnome-settings-daemon to tasks

* Fri Apr 16 2010 Frederic Crozat <fcrozat@mandriva.com> 2010.1-3mdv2010.1
+ Revision: 535397
- do not install evolution-tracker for now, not stable enough

* Thu Apr 15 2010 Frederic Crozat <fcrozat@mandriva.com> 2010.1-2mdv2010.1
+ Revision: 535106
- fix title
- replace beagle with tracker

* Wed Feb 03 2010 Frederic Crozat <fcrozat@mandriva.com> 2010.1-1mdv2010.1
+ Revision: 500168
- Suggests gnome-color-manager

* Mon Oct 05 2009 Frederic Crozat <fcrozat@mandriva.com> 2010.0-3mdv2010.0
+ Revision: 454068
- gnome-volume-manager functions are now provided by nautilus

* Mon Sep 21 2009 Frederic Crozat <fcrozat@mandriva.com> 2010.0-2mdv2010.0
+ Revision: 446445
- Replace pidgin with empathy

* Wed Jun 24 2009 Frederic Crozat <fcrozat@mandriva.com> 2010.0-1mdv2010.0
+ Revision: 388883
- Suggests cheese (Mdv bug #44716)

* Thu Mar 12 2009 Frederic Crozat <fcrozat@mandriva.com> 2009.1-1mdv2009.1
+ Revision: 354234
- Move suggest of gnome-media to task-gnome-minimal
- Remove suggests on nautilus-cd-burner, it is replaced by brasero

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2009.0-6mdv2009.1
+ Revision: 351499
- rebuild

* Mon Oct 27 2008 Pixel <pixel@mandriva.com> 2009.0-5mdv2009.1
+ Revision: 297561
- transform most Requires into Suggests to allow removing those pkgs while still
  keeping task-gnome installed (otherwise it creates many "orphans")

* Fri Sep 26 2008 Frederic Crozat <fcrozat@mandriva.com> 2009.0-4mdv2009.0
+ Revision: 288690
- Move preload suggest to minimal package, and add readahead as well

* Thu Sep 25 2008 Frederic Crozat <fcrozat@mandriva.com> 2009.0-3mdv2009.0
+ Revision: 288121
- Add preload as suggests, reduce login time at startup

* Wed Aug 27 2008 Frederic Crozat <fcrozat@mandriva.com> 2009.0-2mdv2009.0
+ Revision: 276533
- Add more accessibility apps, as suggests
- enforce gnome-power-manager installation

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2009.0-1mdv2009.0
+ Revision: 245405
- reset version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2008.1-5mdv2009.0
+ Revision: 225622
- rebuild

* Wed Apr 02 2008 Frederic Crozat <fcrozat@mandriva.com> 2008.1-4mdv2008.1
+ Revision: 191683
- Suggests brasero (Mdv bug #39721)

* Tue Mar 04 2008 Frederic Crozat <fcrozat@mandriva.com> 2008.1-3mdv2008.1
+ Revision: 178834
- Suggests task-pulseaudio in task-gnome-minimal

* Thu Feb 28 2008 Frederic Crozat <fcrozat@mandriva.com> 2008.1-2mdv2008.1
+ Revision: 176015
- Remove gthumb from dependencies
- Add vino and vinagre
- Rename gaim into pidgin

* Fri Feb 15 2008 Frederic Crozat <fcrozat@mandriva.com> 2008.1-1mdv2008.1
+ Revision: 168768
- Add suggests on nautilus-sendto-bluetooth and nautilus-sendto-evolution (Mdv bug #29336)

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2007-5mdv2008.1
+ Revision: 128245
- kill re-definition of %%buildroot on Pixel's request

  + Frederic Crozat <fcrozat@mandriva.com>
    - Move requirement on bug-buddy into a suggests and move it to task-gnome-minimal


* Wed Mar 28 2007 Frederic Crozat <fcrozat@mandriva.com> 2007-5mdv2007.1
+ Revision: 149245
- Add evince dependency to main package

* Fri Mar 16 2007 Frederic Crozat <fcrozat@mandriva.com> 2007-4mdv2007.1
+ Revision: 144805
- Pull beagle-gui, not beagle
- Pull beagle-evolution
- Remove specfile translation, they are in separate package now

  + Jérôme Soyer <saispo@mandriva.org>
    - Import task-gnome

* Thu Sep 07 2006 Frederic Crozat <fcrozat@mandriva.com> 2007-3mdv2007.0
- Add more applications

* Sat Aug 19 2006 Frederic Crozat <fcrozat@mandriva.com> 2007-2mdv2007.0
- Replace gnopernicus with orca

* Tue Jul 11 2006 Frederic Crozat <fcrozat@mandriva.com> 2007-1mdv2007.0
- Rename gnome2 package as task-gnome-mininal and merge into task-gnome

* Thu Aug 11 2005 Leonardo Chiquitto Filho <chiquitto@mandriva.com> 2006-1mdk
- package created for Mandriva

