<!-- %META:TOPICINFO{author="BobLantz" date="1337839991" format="1.1" reprev="1.1" version="1.1"}% -->
<!-- %META:TOPICPARENT{name="VM-Creation-Notes"}% -->
<!-- Use our custom page layout:
* Set VIEW_TEMPLATE = [MininetView](MininetView)
-->


Old (generally obsolete) VM Creation Instructions:
---------------------------------------------------

For historical reference, the old VM creation instructions are preserved on this page.

<!-- %TOC% -->


Download Debian Lenny
----------------------

Get Debian netinst .iso:
<verbatim>
wget <http://cdimage.debian.org/debian-cd/5.0.4/i386/iso-cd/debian-504-i386-netinst.iso></verbatim>

Other options are at <http://www.debian.org/CD/netinst/> .


New VM
-------

Start Fusion

Click File, then New.

Click 'Use operating system installation disk image file' and find the iso you just downloaded.

Select 'Linux' for the Operating System and 'Debian 5'.

Customize settings:
* Name: Mininet, or your choice
* 4 GB Hard Disk, don't pre-allocate, don't split into 2 GB files (unless this is on a FAT volume)
* 256 MB RAM (though after the install you can go lower, down to 192 MB or less)
* 1 Virtual processor (2 may yield hangs during link teardown)
Start up the Guest VM to begin the install.

Click on install.

Additional params (you may want to change these for your location):
* Language: **English**
* Location: **United States**
* Keyboard: **American English**
* Hostname: **mininet**
* Domain: **localdomain**
* Time zone: **Pacific**
* Partitioning: **Guided, use entire disk**
* Continue with SCSI 1
* All files written to one partition
* Finish partitioning and write all files to disk
* Yes, write all changes to disk
* Root password: **mininet**
* Username: **mininet**
* Password: **mininet**
* United States
* Mirror: ftp.us.debian.org, or whatever's closest
* Proxy if you've got one
* Feedback if you want to
* All profiles (desktop, standard system) **unclicked** to minimize install size
* Install GRUB to MBR: yes
Once the machine boots, login to the console as username mininet, with password mininet.


Setup Sudo Acesss
------------------

Login as root, with password mininet:
<verbatim>
su</verbatim>

Setup visudo. Later instructions will assume sudo use.
<verbatim>
apt-get install sudo</verbatim>

Enter sudoers file:
<verbatim>
visudo</verbatim>

Change sudo defaults, so that the regular user PATH is used with sudo:
<verbatim>
Defaults !env_reset
Defaults env_delete-="PYTHONPATH"</verbatim>

Add sudo access for your username (mininet will be the assumed username going forward). At the bottom, add:
<verbatim>
mininet ALL=NOPASSWD: ALL</verbatim>

Exit back to main username:
<verbatim>
exit</verbatim>


Setup SSH
----------

At this point, you'll probably want to use SSH on the host machine to connect to the VM, for easier copy/paste.
<verbatim>
sudo apt-get install -y ssh</verbatim>

Find the IP:
<verbatim>
sudo ifconfig eth0</verbatim>

At point, you shouldn't need to enter any more commands into the VM console, and should be able to do everything over SSH, enabling you to simply copy and paste commands from this web page.

To save a hostname for this IP, on Mac OS X, modify /etc/hosts. Here is an example line:
<verbatim>
192.168.115.143 mininet</verbatim>

You can now minimize the VM console; it's no longer needed.

To speed up future SSH connections, add your host's public key to the new VM. We assume the key is already generated. On the host:
<verbatim>
ssh-copy-id mininet</verbatim>

Now you should be able to log in without entering a password:
<verbatim>
ssh mininet@mininet</verbatim>


Install Mininet
================


Download Mininet
-----------------

You don't need to install the Mininet Python code just yet; we'll run the included machine setup shell scripts directly.
<verbatim>
sudo apt-get install -y git-core
git clone git://github.com/mininet/mininet.git
</verbatim>


Install System
---------------


### All-at-once

The main script is ~/mininet/util/install.sh, which does the following:
* Install Kernel w/network namespace support
* Install OpenFlow
* Install Mininet dependencies
* Install NOX
* Install Open vSwitch
Run this now: <verbatim>
cd ~/
time ~/mininet/util/install.sh</verbatim>

... then wait for ~20 min.

Reboot to load new kernel:

	sudo reboot

Clean out unneeded kernel stuff:

	~/mininet/util/install.sh -c

Additional setup:
* (Optional) follow instructions to set up [OpenFlow](OpenFlow) regression tests
Jump to the [VM-Setup-Notes](VM-Setup-Notes).


### Piece-by-Piece

Each step in the combined install can be done piece-by-piece. See the all() function at the bottom of mininet/util/install.sh, and run each command with the corresponding -line flag.

For example, to install the kernel w/network namespace support:

Run:
<verbatim>
sudo ~/mininet/util/install.sh -k</verbatim>


Optional: OpenFlow legacy regression test install
---------------------------------------------------

Setup env vars for OpenFlow tests:
<verbatim>
cd ~/
sudo openflow/regress/scripts/install_deps.pl
cp ~/openflow/regress/scripts/env_vars .
vim env_vars
su
source /home/mininet/env_vars</verbatim>

Add to top of /root/.bashrc:
<verbatim>
source /home/mininet/env_vars</verbatim>

Run tests:
<verbatim>
of_user_veth_test.pl</verbatim>


Customize and Verify Mininet
=============================

Go to [VM-Setup-Notes](VM-Setup-Notes) to customize the VM, install and verify Mininet, and then do the [Walkthrough](Walkthrough.md). These instructions should have ensured all required and optional dependencies are installed.


Post-VM-Creation cleanup
=========================

Follow these instructions if you intend to share the VM. They will:

* free up disk space
* remove tmp logs
* clear history:
* remove private ssh keys
* remove authorized keys
* remove Mininet (until release is publicly available)

<verbatim>
sudo ~/mininet/util/install.sh -d</verbatim>

Shut down guest VM and remove lock file (.lck) if needed.

To prevent the " .vmx tries to connect to a non-existent CD-ROM image" error, disconnect the CD-ROM in the VMWare settings.

Also remove any log files in the VM directory:

	rm *.log

Compress externally in the directory you created the VM:
<verbatim>
tar -czf Mininet.tar.gz Mininet.vmwarevm/</verbatim>


Kernel Compilation from scratch
================================

A script in Mininet will built a custom kernel on Debian machines. You could run this from the Mininet VM, even.

	~/mininet/util/kbuild/kbuild

If building from scratch, make sure you have a kernel later than 2.6.29, configured with the following:
<verbatim>
CONFIG_BRIDGE=m
CONFIG_TUN=m
CONFIG_VETH=m
CONFIG_PCNET32=m
CONFIG_NET_NS=y</verbatim>

For kernel 2.6.33+, as of 3/26/10, the tun kmod has bug when used in a network-namespaced process; a patch is included to work around this kernel oops. See ~/mininet/kbuild for the patch.


Disk Usage Notes
=================

Commands to check disk space:
<verbatim>
df -a
sudo du -B1000 --max-depth=1 /</verbatim> -- [Main/BobLantz](../Main/BobLantz) - 24 May 2012
