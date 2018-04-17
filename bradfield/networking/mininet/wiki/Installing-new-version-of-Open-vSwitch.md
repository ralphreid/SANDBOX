The following instruction show how to replace the version of Open vSwitch that comes in the Mininet VM.  This example shows how to upgrade to Open vSwitch 1.10, but the same basic instructions could be used to upgrade to any other version of Open vSwitch.  I'm going to provide two alternatives for the build and install step.

Become root:

    mininet@mininet-vm$ sudo -s

Remove old packages:

    root@mininet-vm# apt-get remove openvswitch-common openvswitch-datapath-dkms openvswitch-controller openvswitch-pki openvswitch-switch

Download and unpack OpenVSwitch 1.10:

    root@mininet-vm# cd /root
    root@mininet-vm# wget http://openvswitch.org/releases/openvswitch-1.10.0.tar.gz
    root@mininet-vm# tar zxvf openvswitch-1.10.0.tar.gz

Build and install option 1 (Binary build and install):

    root@mininet-vm# cd openvswitch-1.10.0/
    root@mininet-vm# ./configure --prefix=/usr --with-linux=/lib/modules/`uname -r`/build
    root@mininet-vm# make
    root@mininet-vm# make install
    root@mininet-vm# make modules_install
    root@mininet-vm# rmmod openvswitch
    root@mininet-vm# depmod -a

Build and install option 2 (Build Debian packages and install):

    root@mininet-vm# cd openvswitch-1.10.0/
    root@mininet-vm# apt-get install build-essential fakeroot
    root@mininet-vm# apt-get install debhelper autoconf automake libssl-dev pkg-config bzip2 openssl python-all procps python-qt4 python-zopeinterface python-twisted-conch dh-autoreconf
    root@mininet-vm# fakeroot debian/rules binary
    root@mininet-vm# cd ..
    root@mininet-vm# dpkg -i openvswitch-common*.deb openvswitch-datapath-dkms*.deb openvswitch-controller*.deb openvswitch-pki*.deb openvswitch-switch*.deb

[TODO: As openvswitch-controller is no longer (after OVS v2.1) packaged and installed by default, some other means of installing openvswitch-controller (for testing purposes) should be documented here.]

The one advantage to using the packages instead of direct binary install is that you can just use the same steps to upgrade to the next version of Open vSwitch.

Then do some post install steps to keep the Open vSwitch Controller from starting automatically on boot:

    root@mininet-vm# /etc/init.d/openvswitch-controller stop
    root@mininet-vm# update-rc.d openvswitch-controller disable

Start OVS server process:

    root@mininet-vm# /etc/init.d/openvswitch-switch start

That should be it.  Once you have finished, you can confirm that you have the latest Open vSwitch installed and the latest kernel module.  You should see something like the example below.

    root@mininet-vm# ovs-vsctl show
    a96f86e7-ca43-487f-b65d-e18b52a64330
        ovs_version: "1.10.0"

    root@mininet-vm# modinfo openvswitch | grep version:
    version:        1.10.0
    srcversion:     90A0BE65A0CF67E0BEA2D57
