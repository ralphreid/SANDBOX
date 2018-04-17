### Basic Workflow

prepare
- download cloud image if it's missing
- write-protect it

build
- create cow disk for vm
- boot it in qemu/kvm with text /serial console
- install Mininet

test
- make codecheck
- make test
	
release
- shut down VM
- shrink-wrap VM
- upload to [s3] storage
