![android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)
![linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

# MExaGEA
Make Exagear Great Again!

# What is purpose of this project?
I (or maybe we, since @Synnek1337 can be interested in project in future) want to provide custom obb builds for Exagear Windows Emulator.
So basically I will make bunch of custom chrooted linux versions (for start Ubuntu 14.04, 16.04 and 18.04) - I will see how they works and go futher and combinations of wine and wine-staging.
Everything will be handled by custom Django-written builder on my xrailgun.xyz VPS. So, pretty much - amazing stuff.

# What about software rendered Mesa3D?
Yes, I remember about that. I will try also to have builds of recent wine commits with mesa3d, but will NOT provide archive for it until I will get donations for bigger VPS SSD disk size.

# Rights
Pretty much Exagear closed its website and doesn't sell anymore Exagear for any ARM system for public, so I assume I can do mods for legal, I'm not even editing source or getting paid for this.

# Future
* Reverse Exagear to provide more better functionality.
* Provide upgrades suggested by communities from for e.g. reddit.
* Do native gpu acceleration under Exagear (no providen acceleration even under XServer XSDL though).
* Automatized scripts or even application to update everything on fly.

# Data collected for now
* It's possible to run custom Ubuntu/wine, as somebody uploaded Ubuntu 16.04 with 4.7 Wine, which hell was slower on HoMM3 multiple times than default version. Person who did it claimed that was working on image via VMWare - why can't we do it via chroot for automation?
* OBB file is just zip version of Linux rootfs.
* ExaShell is utility to launch custom x86-emulated Linux, but I was not testing it.
* Mesa3D software rendering is slow and for some bugs its better to use OpenGL than Dx9 in some games.

# Compatibility of "non-old" games.
* NosTale runs under 1 fps per 15 seconds and crashes on Dx9.
* Tibia 11 detects system as Virtual Machine and doesn't want to run.

### To be continued.
