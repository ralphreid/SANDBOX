### Creating a Mininet VM from a Clean OS Installation

These instructions cover the process of building a Mininet-capable VM from a clean VM installation, using Ubuntu. After completing these setup instructions, see [VM-Setup-Notes](VM-Setup-Notes) to set up your VM.

_Note: If you need to install on distribution other than Ubuntu or Fedora, you are currently on your own, but it should not be hard to get Mininet to work if you install all of its dependencies._

**First, create a new VM** (using VMware, VirtualBox, etc..) 

To keep the VM smaller, use the server variant.  For 2.0.0, we used 64-bit images, and specifically `ubuntu-12.10-server-amd64.iso`, which can be downloaded from the [Ubuntu Quantal page](http://releases.ubuntu.com/quantal/). (You can also use later versions of Ubuntu, Ubuntu desktop, a 32-bit/i386 version, or Lubuntu, etc..)

The Mininet VM uses username: `mininet` and password: `mininet`, but any user/password combo should work as long as it has admin/`sudo` privileges.

**Next, log in to the new VM and do the following**:

    wget https://raw.github.com/mininet/mininet/master/util/vm/install-mininet-vm.sh
    time bash install-mininet-vm.sh

After this completes (about 10 minutes), Mininet should work:

    $ sudo mn --test pingall

**That's it!**

For historical reference, we have also preserved the [Old VM Creation Notes](Old-VM-Creation-Notes).

***

### How we created the Mininet 2.1.0 VM Images

For Mininet 2.1.0, we used the new [[Automated VM Creation and Testing]] script, `build.py`, which creates VM images using `kvm` or `qemu`.

    ~/mininet/util/vm/build.py raring32server
    ~/mininet/util/vm/build.py raring64server

The time it takes for each VM to be created will vary depending on how many things need to be downloaded and other factors. On our slow VM server, this takes 45 minutes or more. If there is already an existing base image, it takes about 12 minutes on my laptop using nested virtualization. The nice thing about this approach is it is a single command to create a zipped `.ovf` file which can be imported into the virtual machine monitor of your choice.

***

### How we created the Mininet 2.0.0 VM Image

In the future, these steps will be automated, but for now there are several manual steps.

1. Created a new VM `mininet-vm` in VMware using the Ubuntu 12.10 server amd64 image with easy install, and `mininet` for all user information and passwords.

2. Customized it by increasing the memory to 1536 MB and naming it `mininet-vm`

3. Booted `mininet-vm` and let easy install complete (~5min)

4. Ran the following commands (~4min):

        wget https://raw.github.com/mininet/mininet/master/util/vm/install-mininet-vm.sh
        time bash install-mininet-vm.sh
        sudo mn --test pingall

6. Shut down and ran the following (~3min):

   *Note: This assumes you're running on a Mac with the
    [VMware OVF Tool](http://www.vmware.com/support/developer/ovf/) installed!!*

        echo "*** Converting to OVF"
        time /Applications/VMware\ OVF\ Tool/ovftool mininet-vm.vmx mininet-vm.ovf
        echo "*** Fixing OVF so it works with VirtualBox" 
        sed -i -e '/vmw:Config/d' mininet-vm.ovf
        echo "*** Updating SHA1 checksums"
        openssl sha1 mininet-vm.ovf mininet-vm-disk1.vmdk > mininet-vm.mf
        echo "*** Moving OVF to its own directory"
        mkdir mininet-ovf
        mv mininet-vm-disk1.vmdk mininet-vm.{mf,ovf} mininet-ovf
        echo "*** Zipping OVF"
        zip -r mininet-ovf mininet-ovf
        mv mininet-ovf.zip mininet-2.0.0-113012-amd64-ovf.zip

7. Uploaded to <https://github.com/mininet/mininet/downloads> (~10min)

   File to upload: `mininet-ovf.zip mininet-2.0.0-113012-amd64-ovf.zip`  
   Short Description: `Mininet 2.0.0 VM - Ubuntu 12.10 server 64-bit - OVF - 11.30.12`  

   While I was waiting for the download, I extracted the zip archive and verified that I could
   import it and run in VirtualBox.

8. Downloaded from <https://github.com/mininet/mininet/downloads> (~10min)

9. Unzipped and imported into VirtualBox (~3min)

10. Booted, logged in, and tested with

        sudo mn --test pingall

11. Profit!

----

I didn't do the following:

1. Removed DHCP leases

        cd /var/lib/dhcp/
        rm *lease*

   This may not be the right thing to do, as it causes the VirtualBox VM boot to hang
   for 60+ seconds at "waiting for network configuration."

2. Shut down VM and added an additional private (host-only) network interface.

   This also didn't seem to work as the OVF was imported into VirtualBox with only one interface.