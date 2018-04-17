We now have the ability to automatically build and test Mininet VM images.

#### Automated VM Creation

The `mininet/util/vm/build.py` script can automate creation of `.ovf` VM images as follows:

    build.py raring32server

`build.py` takes a list of build flavors, which may be listed using

    build.py --list

Important notes:

* **By default, `build.py` will create a `vmtest` directory in your home directory** and store cached ISOs and base VM images there. This feature is not configurable at this time.

* The first time a new flavor is used, its ISO installer image will be downloaded and a base image will be created (i.e. a basic Ubuntu installation including the `mininet` user.)

* If the base image is already there, it will be reused as the base image for the copy-on-write `.qcow2` image created during the build process.

* VM images and ISOs are large and can fill up your storage very quickly.

* By default, `build.py` creates a `.qcow2` disk image and converts it into a `.vmdk` image, which can be used by (kvm, VirtualBox, VMware, etc.)

* By default, the `.qcow2` image is deleted after it is converted into a `.vmdk`; if you specify the `--qcow2` option, then that image will not be deleted (but the `.vmdk` will still be created.)

* By default, VM output (from base image creation as well as Mininet VM installation) is logged to log files; specifying the `-v` (`--verbose`) option overrides this behavior and logs VM output to the console; this can make it easier to monitor the progress of the script if it is being run interactively.

* By default, the script uses `kvm` with hardware acceleration; I routinely use this within a VMware VM using the nested virtualization feature of VMware Fusion (which you need to enable in the VM's processor settings.) You can test whether `kvm` can be used by using the command `kvm-ok`. If `kvm` cannot be used, you can revert to `qemu`'s TCG emulation by specifying the `-n` (`--nokvm`) option to `build.py`. Note that software emulation may be *much* slower than hardware virtualization, but it should still work (although performance-sensitive tests such as `test_hifi` may fail.)

#### Automated VM testing

Once a VM image has been created, it can also be booted automatically for additional testing.

The `build.py` script also has the ability to test existing VM images. For example:

    build.py --image mininet-raring32server.vmdk --test core

will boot a VM from disk image `mininet-raring32server.vmdk` and run the `core` test. (`build.py -h` will list available tests.)

Additionally, you can specify a branch to check out and test in the VM, for example

    build.py --image mininet-vm.vmdk --branch devel/myfeature --test sanity

would boot from the specified image, check out the `devel/myfeature` branch from the Mininet github repository, and run the `sanity` test.


Notes:

* Currently the script runs a simple sanity test (`--test pingall`) as well as the Mininet core tests (`make test`); the entire boot and test completes in less than 90 seconds on my laptop.

* In the future, we will add the option to specify additional (and lengthier) tests.

* As part of the boot, the kernel and initial RAM disk (initrd) are extracted from the image; this is necessary so that we can boot the VM with a serial console for `pexpect`

* The base disk image should be unaffected by the test process, since it is only used as backing store for a COW (copy-on-write) image, which is used for all changes to the file system and is deleted after VM shutdown.

* The boot and test procedure creates a temporary directory for temporary files (kernel, initrd, COW image) and deletes if upon completion.




