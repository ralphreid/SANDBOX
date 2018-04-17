Project Ideas for Mininet
---
#### Table of Contents

<!--

This is the script that I used to generate the TOC from the html of this page:

#!/usr/bin/python

from fileinput import input
import re

r1 = re.compile( r'href=\"(#[^\"]+).*</a>([^<]*)</h2>' )
r2 = re.compile( r'href=\"(#[^\"]+).*</a>([^<]*)</h3>' )

prefix='https://github.com/mininet/mininet/wiki/Ideas'

for line in input():
    line = line.strip()
    m = r1.search( line )
    if m:
        print '1. [%s](%s%s)' % ( m.group( 2 ), prefix, m.group( 1 ) )
        continue
    m2 = r2.search( line )
    if m2:
        print '  * [%s](%s%s)' % ( m2.group( 2 ), prefix, m2.group( 1 ) )

-->

<!-- TOC: Please keep this up to date; the script above is provided for assistance!! -->

1. [Project Ideas for Mininet](https://github.com/mininet/mininet/wiki/Ideas#wiki-project-ideas-for-mininet)
1. [Mininet Project Ideas](https://github.com/mininet/mininet/wiki/Ideas#wiki-mininet-project-ideas)
1. [Background](https://github.com/mininet/mininet/wiki/Ideas#wiki-background)
1. [GSoC 2015 Possibility](https://github.com/mininet/mininet/wiki/Ideas#wiki-gsoc-2015-possibility)
1. [Mininet Development Process](https://github.com/mininet/mininet/wiki/Ideas#wiki-mininet-development-process)
1. [Making it Real: extending existing prototype code into an official feature](https://github.com/mininet/mininet/wiki/Ideas#wiki-making-it-real-extending-existing-prototype-code-into-an-official-feature)
  * [Hardware interface support](https://github.com/mininet/mininet/wiki/Ideas#wiki-hardware-interface-support)
  * [Access into Mininet from host and/or local network](https://github.com/mininet/mininet/wiki/Ideas#wiki-access-into-mininet-from-host-andor-local-network)
  * [sshd support](https://github.com/mininet/mininet/wiki/Ideas#wiki-sshd-support)
  * [Mininet GUIs: consoles.py and miniedit.py](https://github.com/mininet/mininet/wiki/Ideas#wiki-mininet-guis-consolespy-and-minieditpy)
  * [Automatic NAT implementation](https://github.com/mininet/mininet/wiki/Ideas#wiki-automatic-nat-implementation)
1. ["Easier" Projects](https://github.com/mininet/mininet/wiki/Ideas#wiki-easier-projects)
  * [Mininet error checking and diagnostics/status monitoring](https://github.com/mininet/mininet/wiki/Ideas#wiki-mininet-error-checking-and-diagnosticsstatus-monitoring)
  * [Better X11 support](https://github.com/mininet/mininet/wiki/Ideas#wiki-better-x11-support)
  * [Easier VM image creation (e.g. using something like ubuntu-vm-builder)](https://github.com/mininet/mininet/wiki/Ideas#wiki-easier-vm-image-creation-eg-using-something-like-ubuntu-vm-builder)
  * [Real API documentation explaining how to use the API (will be helped somewhat by integrating CS244 intro document)](https://github.com/mininet/mininet/wiki/Ideas#wiki-real-api-documentation-explaining-how-to-use-the-api-will-be-helped-somewhat-by-integrating-cs244-intro-document)
  * [Automatic/easy update for Mininet (esp. in VM image)](https://github.com/mininet/mininet/wiki/Ideas#wiki-automaticeasy-update-for-mininet-esp-in-vm-image)
  * [Additional easy (but non-critical)  bug fixes](https://github.com/mininet/mininet/wiki/Ideas#wiki-additional-easy-but-non-critical--bug-fixes)
  * [Patch bay object](https://github.com/mininet/mininet/wiki/Ideas#wiki-patch-bay-object)
  * [“testbed mode” - Hosts optionally on both control and data networks](https://github.com/mininet/mininet/wiki/Ideas#wiki-testbed-mode---hosts-optionally-on-both-control-and-data-networks)
  * [Additional parametrized topologies (fat tree, jellyfish, mesh, random, etc.) bundled with easy controller support for multipath](https://github.com/mininet/mininet/wiki/Ideas#wiki-additional-parametrized-topologies-fat-tree-jellyfish-mesh-random-etc-bundled-with-easy-controller-support-for-multipath)
  * [Raspberry Pi Mininet image/"network in a box" ;-)](https://github.com/mininet/mininet/wiki/Ideas#wiki-raspberry-pi-mininet-imagenetwork-in-a-box--)
1. ["Advanced"/more challenging projects](https://github.com/mininet/mininet/wiki/Ideas#wiki-advancedmore-challenging-projects)
  * [More sample, downloadable SDN systems (including controller and applications)](https://github.com/mininet/mininet/wiki/Ideas#wiki-more-sample-downloadable-sdn-systems-including-controller-and-applications)
  * [Enhanced placement and documentation for Mininet examples](https://github.com/mininet/mininet/wiki/Ideas#wiki-enhanced-placement-and-documentation-for-mininet-examples)
  * [Cluster mode - supporting execution over multiple machines (RemoteSwitch,L2TP/VDE/VXLAN/Capsulator, etc.)](https://github.com/mininet/mininet/wiki/Ideas#wiki-cluster-mode---supporting-execution-over-multiple-machines-remoteswitchl2tpvdevxlancapsulator-etc)
  * [Hybrid network support (API for hardware, virtual and combo network tests)](https://github.com/mininet/mininet/wiki/Ideas#wiki-hybrid-network-support-api-for-hardware-virtual-and-combo-network-tests)
  * [Seamless migration between Mininet and hardware](https://github.com/mininet/mininet/wiki/Ideas#wiki-seamless-migration-between-mininet-and-hardware)
  * [Mininet control of real hardware](https://github.com/mininet/mininet/wiki/Ideas#wiki-mininet-control-of-real-hardware)
  * [Automated deployment on EC2](https://github.com/mininet/mininet/wiki/Ideas#wiki-automated-deployment-on-ec2)
  * [Automated deployment on other testbeds? (emulab, geni, etc.)](https://github.com/mininet/mininet/wiki/Ideas#wiki-automated-deployment-on-other-testbeds-emulab-geni-etc)
  * [Automated creation of virtual network based on real network](https://github.com/mininet/mininet/wiki/Ideas#wiki-automated-creation-of-virtual-network-based-on-real-network)
  * [Mininet network debugger (ndb)?](https://github.com/mininet/mininet/wiki/Ideas#wiki-mininet-network-debugger-ndb)
  * [Code refactoring including Mininet core which could be used independently](https://github.com/mininet/mininet/wiki/Ideas#wiki-code-refactoring-including-mininet-core-which-could-be-used-independently)
  * [Error recovery using Python's with statement (Mininet 3.0?)](https://github.com/mininet/mininet/wiki/Ideas#wiki-error-recovery-using-pythons-with-statement-mininet-30)
  * [Measured scalability results (and possibly improved scalability)](https://github.com/mininet/mininet/wiki/Ideas#wiki-measured-scalability-results-and-possibly-improved-scalability)
  * [Provisioning advice and/or automatic provisioning support](https://github.com/mininet/mininet/wiki/Ideas#wiki-provisioning-advice-andor-automatic-provisioning-support)
  * [Integrated (emulator and emulated) performance monitoring](https://github.com/mininet/mininet/wiki/Ideas#wiki-integrated-emulator-and-emulated-performance-monitoring)
  * [Mininet validation against hardware testbeds](https://github.com/mininet/mininet/wiki/Ideas#wiki-mininet-validation-against-hardware-testbeds)
  * [Other OS support: Debian Wheezy, Fedora Core, BSD? OS X? Windows?](https://github.com/mininet/mininet/wiki/Ideas#wiki-other-os-support-debian-wheezy-fedora-core-bsd-os-x-windows)
  * [Link (e.g. wire or wireless) simulator support](https://github.com/mininet/mininet/wiki/Ideas#wiki-link-eg-wire-or-wireless-simulator-support)
  * [Ability to more compactly package Mininet networks and download into VM](https://github.com/mininet/mininet/wiki/Ideas#wiki-ability-to-more-compactly-package-mininet-networks-and-download-into-vm)
  * ["Pure" Python implementation (need to determine the performance hit)](https://github.com/mininet/mininet/wiki/Ideas#wiki-pure-python-implementation-need-to-determine-the-performance-hit)
  * [Enhanced unit tests](https://github.com/mininet/mininet/wiki/Ideas#wiki-enhanced-unit-tests)
  * [Enhanced system tests](https://github.com/mininet/mininet/wiki/Ideas#wiki-enhanced-system-tests)
  * [Automatic testing of examples/](https://github.com/mininet/mininet/wiki/Ideas#wiki-automatic-testing-of-examples)
  * [Performance analysis and fixes to the Linux kernel and Open vSwitch](https://github.com/mininet/mininet/wiki/Ideas#wiki-performance-analysis-and-fixes-to-the-linux-kernel-and-open-vswitch)
  * [Virtual time via time-dilation](https://github.com/mininet/mininet/wiki/Ideas#wiki-virtual-time-via-time-dilation)
  * [Virtual time via barrier synchronization](https://github.com/mininet/mininet/wiki/Ideas#wiki-virtual-time-via-barrier-synchronization)
  * [Different modes of operation to trade of emulation speed vs. performance accuracy](https://github.com/mininet/mininet/wiki/Ideas#wiki-different-modes-of-operation-to-trade-of-emulation-speed-vs-performance-accuracy)
  * [Higher-performing switches (e.g. VALE-enabled OVS and/or custom switch)](https://github.com/mininet/mininet/wiki/Ideas#wiki-higher-performing-switches-eg-vale-enabled-ovs-andor-custom-switch)
  * [Support for private /etc directory and possibly private filesystem, user space, PID space, etc.](https://github.com/mininet/mininet/wiki/Ideas#wiki-support-for-private-etc-directory-and-possbly-private-filesystem-user-space-pid-space-etc)


---

## Mininet Project Ideas

This page summarizes various ideas for features and future functionality for Mininet. It may be used as source material for potential features for any Mininet developer (or motivated user!) to implement, as well as potential projects for Google Summer of Code or other mentoring programs or internships.

## Background

[Mininet](http://mininet.github.com) is a lightweight emulator for computer networks and distributed systems, giving you a stack of "virtual hardware" inside your laptop that you can use for prototyping and developing your own experiments, applications, and systems. Mininet starts up a virtual network/distributed system of servers, switches, and OpenFlow controllers in a few seconds, with a single command, and provides an extensive Python API for emulating almost any Linux-based network system you can imagine (though perhaps at lower speed or smaller scale.) It is widely used for network research, teaching, and development, particularly in the area of OpenFlow and Software-Defined Networking, where it is a key component of an emerging SDK for SDN. It is available under a liberal BSD-style license and is included in Ubuntu as the [`mininet`](https://launchpad.net/ubuntu/+source/mininet) package.

## Mininet Development Process

Mininet follows a fairly standard development process on Github:

0. Review the [[Mininet Python Style]] guidelines.

1. Pick a **project to work on** or a **feature to implement**

2. **Check** the [Mininet issues page](https://github.com/mininet/mininet/issues) to see if someone is already working on it.

3. If so, **contact the person who is working on it**, and also **add a note to the issue** when you start working on it. Optionally drop us a line on
[`mininet-dev`](https://mailman.stanford.edu/mailman/listinfo/mininet-dev) or
[`mininet-discuss`](https://mailman.stanford.edu/mailman/listinfo/mininet-discuss). 
You may also add a note to the appropriate section on this page. The goal is to **avoid duplicating effort** unnecessarily!

4. **Fork/clone** the Mininet repo (master branch) on github, and work on your new feature

5. When you have something that is working or are ready for feedback on your feature, submit a **pull request**.

6. **Respond** any questions or comments you may get on the pull request, and **revise your code** as necessary.

7. If you have specific (and intelligent/well-resarched) development questions that you cannot answer on your own, send them to the [`mininet-dev`](https://mailman.stanford.edu/mailman/listinfo/mininet-dev) or [`mininet-discuss`](https://mailman.stanford.edu/mailman/listinfo/mininet-discuss) mailing lists as appropriate. You can (and probably should!) also **ask for additional feedback** on your code/pull request.

8. When/if the feature is complete and approved by the Mininet developers, they may choose to merge it into the main Mininet source tree (either master or a development branch)!! Congratulations, you are now an official Mininet contributor!!

## GSoC 2015 Possibility

**NOTE: Unfortunately we will not be participating in Google Summer of Code 2014. However, we may rejoin GSoC in 2015, so stay tuned!**

Mininet is an interesting and high-impact project which is also fun to work on, and we're excited to be applying to the Google Summer Of Code (GSoC) in the hope of attracting energetic and motivated developers.

**Mentoring**: A participant in GSoC would choose one or more projects and be advised by a project mentor, either one of the core [Mininet developers](https://github.com/mininet?tab=members) or another contributor to the project.

**Projects**: 
We have identified a wide variety of potential GSoC projects for Mininet, and the current, detailed list is available at the Ideas page on the Mininet wiki at http://github.com/mininet/mininet/wiki/Ideas

Projects are grouped by complexity/difficulty as well as whether we have starter code. The project(s) will be selected by agreement between the potential mentor(s) and participant(s), based on participant interest, experience and knowledge, as well as project impact, project difficulty, and mentor availability and interest.

**General Prerequisites**: In general, working on Mininet requires knowledge of Python and a sound understanding of computer networks, operating systems, and distributed systems (preferably at the undergraduate, masters or professional level.) Other specific projects may require knowledge of C and Unix/Linux systems programming and possibly kernel programming as well. And of course the main prerequisites are energy, enthusiasm, and the ability and desire to use your brain, to learn, and to teach yourself by doing background research (including reading documentation, reading code, trying out ideas, and finding and consulting on-line and off-line references). And writing code and using git/github of course.

Specific prerequisites for each project are listed as well - these are the requisite skills and knowledge that you will need (or need to acquire) to actually complete the tasks for the project.

**Process**: GSoC projects will follow the standard [Mininet development process](https://https://github.com/mininet/mininet/wiki/Ideas#mininet-development-process) .


## Making it Real: extending existing prototype code into an official feature

### Hardware interface support

**Brief explanation**: It's useful to be able to add hardware interfaces to a Mininet network, and also to integrate a Mininet network into a "real" network. Currently examples/hwintf.py contains code demonstrating how to add a "real" hardware interface (or any interface not created/controlled by Mininet) to a Mininet switch. Unfortunately, hardly anyone on the  mailing list seems to be able to understand it or use it, usually because they don't have a good understanding of the principles or practical aspects of IP networking or Linux.

**Questions and additional information**: do we need a better API for this? Do we need better example code? Do we need resources to help users improve their (often meager) skills?

It would certainly be nice to have an easy mechanism for plugging a Mininet virtual network into a physical network. Is there an easy way to provide some mechanism? A problem is that it usuallly requires configuration of network switches/routers, something which is beyond the scope of Mininet (or is it?) 
Access to “real” Internet from mininet network (e.g. extra interfaces)

A common complaint from Mininet users is that "Google doesn't work" or "apt-get doesn't work." This complaint usually indicates a fundamental misunderstanding of Mininet's default configuration:  by default, Mininet gives you a 10.x data network which is not connected to the outside world. This is often a good thing! However, this is not what many users expect - most real networks connect to the internet, after all. It would be easy to follow Emulab's approach of giving each host two interfaces, one for the (internal, OpenFlow-controlled) data network, and one on the LAN. However, there are issues: how are LAN addresses assigned? Can we assume that there is a DHCP server and that there are enough IP addresses on the LAN segment for Mininet hosts? Or should we implement a local network with NAT to allow Mininet hosts to share the Linux host's LAN IP address? Probably we want both, but I suspect that the NAT approach is more likely to be what most people would want. See "Automatic NAT Iimplementation", below.

**Expected results**: A simple and robust API for integrating real hardware interfaces into a Mininet network.

**Knowledge prerequisite**: Understanding of Linux/IP networking, VM network bridging, Mininet and Python.

### Access into Mininet from host and/or local network

On the other hand, it's also useful to be able to connect into the Mininet network either from the host or the  LAN. sshd.py shows how to create an interface on the local host (in the root namespace) which is connected to a Mininet switch, and also how to start up sshd on each Mininet host so that you can ssh into the Mininet network.

**Expected results**: A command-line option for `mn` which automatically provides access to the Mininet network from the host or LAN.

**Knowledge prerequisite**: Understanding of Linux/IP networking, VM network bridging, Mininet and Python.

### sshd support

**Brief explanation**:It might be nice to have a means of automatically starting up sshd (and shutting it down!) on each Mininet host. As noted above, sshd.py has a prototype implementation for this feature, but getting it right, reliable, etc. is actually tricky. There's another more subtle issue and that is: what is the best way to enable seamless transitions between Mininet and hardware? Hardware systems are often bound together using ssh/sshd, so does it make sense to have a Mininet network work that way (ssh and paramiko in Python?) Unfortunately this would increase overhead and startup time, and one of the huge benefits of Mininet is that it starts up very quickly for a highly efficient edit-run-debug loop.

**Expected results**: A command-line option for `mn`, and either an API or extension to the `Mininet` class which automatically starts up (and shuts down) `sshd` on each Mininet host; possibly this would be integrated with the above function of providing access to Mininet hosts from the local host or LAN.

**Knowledge prerequisite**: Understanding of Linux/IP networking, VM network bridging, Mininet and Python.

### Mininet GUIs: consoles.py and miniedit.py

**Status**: Gregory Gee has been working on an enhanced version of MiniEdit.

**Brief explanation**: I (BL) wrote the consoles.py and miniedit.py examples to show what I thought was a really exciting and cool thing you could do in Mininet: make GUI programs that create and use a live virtual network interactively! It seemed so obvious that I had done much of the hard work and that any smart Python/GUI programmer could take what I had done either as code or inspiration and run with it. Unfortunately, that never happened. We could decide to expand these programs into (more) full-blown applications, or we could also try to make the code reusable as a framework. Or we could write documentation about the design of the apps and how to expand them. Or perhaps we could rewrite them in Qt or a more "modern" GUI framework. Regardless, I still feel that GUI apps using Mininet have huge potential, as do graphical interfaces for core Mininet functionality.

**Expected results**: significantly more beautiful, functional, robust and useful consoles.py and miniedit.py applications. In the case of consoles.py, it should provide a useful API for building monitoring applications. In the case for miniedit.py, it should be able to save and load networks as mininet-compatible topologies (expressed in Python.)

**Knowledge prerequisite**: Understanding of Linux/IP networking, Mininet, Python, OpenFlow and TkInter and/or another GUI framework. HCI/user-interface design abilities.

### Automatic NAT implementation

**Brief explanation**: As noted above, an automatic NAT implementation (e.g. nat=True or --nat) would be nice to have to enable Mininet hosts to talk to the outside world by default.

**Expected results**: A command-line option for `mn`, and probably an option to `Mininet()`, which provides automatic creation of a NAT which allows transparent, seamless access to the LAN and the internet from Mininet hosts.

**Knowledge prerequisite**: Understanding of Linux/IP networking, VM network bridging, IPTables, NAT, Mininet and Python.

## "Easier" Projects

### Mininet error checking and diagnostics/status monitoring

**Brief explanation**: Currently when Mininet isn't working (e.g. controller can't connect to switches, or packets aren't being forwarded in your network), the only indication that something is wrong is that ping doesn't work. It would be nice to have some means of verifying network health, for example, by monitoring whether all switches are connected to controllers, or by checking that all links in the system work somehow. The former would be easy(ish?), the latter hard.

**Expected results**: A command-line option for `mn` which automatically provides access to the Mininet network from the host or LAN.

**Knowledge prerequisite**: Understanding of Linux/IP networking, VM network bridging, Mininet code base and Python. Usage-level understanding of Open vSwitch and the OpenFlow reference switch.

### Better X11 support

**Brief explanation**: It should be possible to start up arbitrary X11 apps from the mininet> prompt.

**Difficulty**: Trivial. ;-)

**Expected results**: A CLI command for starting X11 apps

**Knowledge prerequisite**: Understanding of Mininet API and CLI code base and X11.

### Easier VM image creation (e.g. using something like ubuntu-vm-builder)

**Status**: `build.py` script implemented in 2.1.0.

**Brief explanation**: Currently we make the VM images by hand - it's a pain, and it's why the Mininet VMs are rarely updated. We could automate this by using a script like the now-deprecated ubuntu-vm-builder, which was part of Ubuntu and used debuild. Or we could script Xen/KVM/VMware/Vbox to take an off-the-shelf Ubuntu image and install Mininet in it. There might be other better ways.

**Expected results**: Modified Mininet makefiles which include a target to build a VM image.

**Knowledge prerequisite**: Understanding of VM creation and things like debuild, chroot; understanding of Linux/Unix tools like Make, shell scripting, possible Python scripting.

### Installing NOX 2 and/or other controllers from `install.sh`

**Brief explanation**: We currently install POX rather than NOX classic by default with install.sh -a (which is intended to create a VM image for the OpenFlow tutorial.) It might be nice to add NOX2 or other useful software.

**Expected results**: Additional options in `install.sh` to install additional controllers or other useful software.

**Knowledge prerequisite**: Understanding of Mininet, OpenFlow controllers, Linux software installation, and shell scripting.

### Real API documentation explaining how to use the API (will be helped somewhat by integrating CS244 intro document)

**Brief explanation**: CS244's Introduction to Mininet has been revised and moved into the Mininet wiki on github. However, we're still lacking in high-quality documentation describing the overall API (and system) architecture as well as how to use the low-, mid- and high-level APIs. Ultimately I'd like to see high quality documentation (think Python, Smalltalk-80: The Language and its Implementation, or Computer Architecture: A Quantitative Approach) but something of O'Reilly quality might be a nice stopgap.

**Expected results**: A document describing the API and system architecture.

**Knowledge prerequisite**: Familiarity with Python and the Mininet API. Ability to write Mininet scripts. Ability to read and understand Python APIs and to write clear and thorough documentation.

### Automatic/easy update for Mininet (esp. in VM image)

**Brief explanation**: If there were an easy way to update Mininet in the VM image, then we might not have to update the whole VM image simply for a Mininet change. Perhaps the tutorial image should update Mininet the first time it boots up? Or maybe we should add update instructions to the OpenFlow tutorial?

**Difficulty**: Easy/trivial.

**Expected results**: A Mininet VM which either automatically updates itself or updates itself to the latest  tutorial version of Mininet with a single command.

**Knowledge prerequisite**: Familiarity with Mininet, git, shell scripting, and Python, as well as VM creation. A more advanced version of this project might integrate with automatic VM creation.

### Additional easy (but non-critical)  bug fixes

**Brief explanation**: There are a number of easy(ish) bug fixes which were deferred from 2.0.0. We can probably identify them and fix them.

**Expected results**: Swatting flies - resolving a number of easier bugs in Mininet (based on interest, importance, ability and complexity of bugs. Ideally this would also include creation of regression tests to determine that the bugs no longer occur.

**Knowledge prerequisite**: Familiarity with Python and the Mininet code base. Ability to write Mininet scripts. Ability to read and understand Python APIs and to use github.

### Patch bay object

**Brief explanation**: Mininet 2.0 switches support attachment and reattachment. This allows you to simulate mobility or VM migration. A more generalized mechanism might allow for everything to be connected to a patch bay/patch panel object (probably just a large OpenFlow switch) which could be used to allow arbitrary reconnection of any interfaces. Effectively this means that each veth pair is split into two veth pairs which are then plugged into the patch bay. This would require creation of a new object (PatchBay?) and support for using it if desired. Note that the overall system load would be increased - this is a trade-off between flexibility and performance, so we would not wish to make it mandatory. This could also be thought of as an L1 switch, although really it's L1.5 since everything is still Ethernet - the L2/MAC protocol cannot be changed beyond what OpenFlow already allows you to do.

**Expected results**: A new Patchbay object and API for Mininet, as well as documentation, tests, and examples.

**Knowledge prerequisite**: Familiarity with Python and the Mininet API. Ability to write Mininet scripts. Ability to read and understand Python APIs and to write clear and thorough tests and documentation.

### “testbed mode” - Hosts optionally on both control and data networks

**Brief explanation**: As noted, Emulab and other testbeds provide (at least) two interfaces on each host: one on the private data network, and one on either a control network or the LAN. This would, to some extent, solve the problem of people who want to access the internet from Mininet hosts, and it would allow network-based (as upposed to pipe or API-based) access to hosts even when the data network was not working.

**Expected results**: An API and command-line options for supporting this configuration, as well as examples and/or tests for same.

**Knowledge prerequisite**: Familiarity with Python and the Mininet API. Ability to write Mininet scripts. Ability to read and understand Python APIs and to write clear and thorough documentation.

### Additional parametrized topologies (fat tree, jellyfish, mesh, random, etc.) bundled with easy controller support for multipath

**Brief explanation**: Parametrized topologies are one of Mininet's most useful features. Unfortunately only a few topologies (tree, linear, single switch) are included in the box. It would be great if Mininet came with more topologies and if there were a readily available controller that supported multipath. We can probably leverage the CS244 work to some extent, since Brandon provided a fat tree topology as well as a simple multipath controller (riplpox) - both of which were extremely handy in CS244. Additionally, two of the CS244 projects included Jellyfish and DCell, so perhaps they have topology code we could use or use as inspiration.

**Expected results**: New topologies for Mininet (Topo() subclasses) as well as examples/system-level tests of same

**Knowledge prerequisite**: Familiarity with Python and the Mininet API. Ability to write Mininet scripts. Understanding of networks, OpenFlow, SDN and controllers (e.g. POX.) Ability to read and understand Python APIs and to write clear and thorough documentation.

### Raspberry Pi Mininet image/"network in a box" ;-)

**Status**: It should be possible to leverage the existing `build.py` script to automatically boot a Raspbian (or other OS) image (using `qemu` in ARM emulation mode) and install Mininet.

**Brief explanation**: This would be a fun and cool project and would also allow for a very inexpensive "network in a box" which could be used not only as a dirt-cheap Mininet platform (for courses, workshops, tutorials, anyone who wants one) but also as virtual "hardware" which you can plug your PC, server, or switches into to get a larger virtual topology. The basics are extremely easy, but there are some interesting and fun possibilities here.

**Difficulty**: Trivial to Easy

**Expected results**: A downloadable, bootable Raspberry Pi image and/or package for Mininet.

**Knowledge prerequisite**: Familiarity with Mininet as well as the Linux build environment, including makefiles, shell scripts, kernel builds, and debian packaging.

## "Advanced"/more challenging projects

### More sample, downloadable SDN systems (including controller and applications)

**Brief explanation**: One of the main goals of Mininet was to enable people to easily share networks and build upon the work of others. To some extent this was realized in CS244 and our blog, reproducingnetworkresearch.wordpress.com. However, we don't currently have a repository (besides EC2) for people to contribute downloadable images and systems that people can easily download and use. It would be nice to have this and to have it linked from the web site. 

**Expected results**: A repository and a means for submitting Mininet-based systems, and a basic set of Mininet-based systems that people can click, download, and run!!

**Knowledge prerequisite**: Familiarity with Mininet and network systems experiments, including OpenFlow/SDN based systems. Familiarity with Linux, shell scripting, Python, web programming/JavaScript/REST, and the ability to use systems like Amazon EC2 and S3.

### Enhanced placement and documentation for Mininet examples

**Brief explanation**: Additionally, people frequently seem to be unaware of the examples and/or have trouble understanding them. It would be nice to document them and to place them more prominently in the documentation and/or on the web site. Eventually it woud be nice to have a sequence of tutorial examples, not just for Mininet but for SDN and Openflow in general

**Expected results**: Better documentation of the Mininet examples, better and better-documented example code, and additional examples. Potentially this documentation could/should take the form of tutorials explaining how to use the examples, along with questions/suggested exercises for extending them.

**Knowledge prerequisite**: Familiarity with Python and the Mininet API. Completion of all Mininet and OpenFlow tutorials. Ability to clearly write code and documentation.

### Cluster mode - supporting execution over multiple machines (RemoteSwitch,L2TP/VDE/VXLAN/Capsulator, etc.)

**Status**: Vitaly Antonenko, Philip Wette, and Bob Lantz have been attacking this project from slightly different angles.

**Brief explanation**: This is probably the biggest missing feature of Mininet, and something which was planned since day one but never actually completed. We would like to be able to create very large Mininet networks by using a cluster of machines. This means we need a way to easily start up Mininet instances on multiple machines and to wire them together into a larger simulation. This should be as transparent as possible so that the cluster just appears to be a larger machine running Mininet.  (Of course there is no longer a single clock domain, and other differences may leak through, but in general the same code should run on a single machine or on a cluster.)

**Expected results**: A version of Mininet which seamlessly and reliably runs on clusters of machines, along with tests, examples, documentation, and performance/scalability measurements.

**Knowledge prerequisite**: Familiarity with Python and the Mininet internal architecture. Understanding of Linux and Ethernet/IP networking, switching/routing and tunneling. Understanding of Linux, distributed systems, and performance measurement/debugging. Ability to write clear examples and documentation.

### Hybrid network support (API for hardware, virtual and combo network tests)

### Seamless migration between Mininet and hardware

### Mininet control of real hardware

**Brief explanation**: These three features are probably variants of the same feature. Basically we would like to be able to integrate hardware components into a Mininet network and control both hardware and virtual components via the same standard Mininet API. Seamless migration means that the same setup scripts should be usable whether Mininet or a hardware testbed are being used. Note that Emulab and ns-2 are a bit ahead of us in that regard in that v-Emulab, hardware Emulab, and ns-2 all use the same basic Tcl script format for setting up experiments. (However, those scripts are not generally usable on hardware which isn't Emulab.)

**Expected results**: APIs, examples, documentation and tutorials for an end-to-end example of the above. The more general the functionality, the better.

**Knowledge prerequisite**: Understanding of Ethernet/IP/Software-defined networking in both hardware (e.g. NEC OpenFlow switches) and software (e.g. Open vSwitch) form. Understanding of Mininet philosophy and internal architecture. Python programming.

### Automated deployment on EC2

**Brief explanation**: This is similar to the above - it would be nice to be able to spawn a simulation across multiple EC2 nodes semi-automatically.

**Expected results**: Scripts and/or command-line options for `mn` to easily run Mininet on EC2, along with examples, documentation and tutorials. Ideally there would also be a Python API to make this easier.

**Knowledge prerequisite**: Understanding of Mininet API and internals, Python programming, possibly shell scripting/programming; ability to use EC2 and its APIs.

### Automated deployment on other testbeds? (emulab, geni, etc.)

**Brief explanation**: Since there are already a number of provisioning APIs (including Emulab, GENI/FOAM, and OpenStack), perhaps it would be nice to ease migration between Mininet and those hardware testbeds (or a simple cluster of PCs with Ubuntu or another standard Linux distribution and no special software installed.)

**Expected results**: Scripts and/or command-line options for `mn` to easily run Mininet on at least one of the above hardware testbeds along with examples, documentation and tutorials. Ideally there would also be a Python API to make this easier.

**Knowledge prerequisite**: Understanding of Mininet API and internals, Python programming, possibly shell scripting/programming; ability to use the appropriate testbed and provisioning APIs.

### Automated creation of virtual network based on real network

**Brief explanation**: It would be quite neat to be able to discover the topology of a physical, hardware network and to recreate it automatically in Mininet.

**Expected results**: Example code, documentation, and tutorials for automatically discovering and recreating a hardware topology in Mininet.

**Knowledge prerequisite**: Understanding of Mininet API and internals, Python programming, and probably OpenFlow/SDN as well as at least one controller framework (e.g. POX, Floodlight, etc..)

### Mininet network debugger (ndb)?

**Brief explanation**: NetSight/ndb were built on top of Mininet. If we want to create an SDN SDK, it would be nice to make it as easy as possible to install and run ndb.

**Expected results**: Installation as well as scripts and/or an API and command-line options for easily deploying and running ndb on a Mininet infrastructure.

**Knowledge prerequisite**: Understanding of Mininet API and internals, Python programming, OpenFlow/SDN networks and debugging as well as Netsight and ndb.

### Code refactoring including Mininet core which could be used independently

**Brief explanation**: The core of Mininet is very simple, but it has become more complicated as we have added more features to it. As a reaction to this, one Mininet user created Piconet, which is reminiscent of the original Mininet. But, it lacks many of the good features that we know and love about Mininet (one command line to rule them all, parametrized topologies, etc..) It would be nice to make the Mininet design more modular so that you could have a simplified core/microkernel of Mininet which could be used independently, along with modules which you could add as desired.

**Expected results**: A version of Mininet with a refactored core which is simpler and easier to understand and which can be used standalone.

**Knowledge prerequisite**: Understanding of Mininet API and internals, Python programming.

### Error recovery using Python's with statement (Mininet 3.0?)

**Brief explanation**: Another excellent design decision in Piconet was to use Python's with statement for automatic recovery and cleanup. We should adopt this as well. Although it would require API changes, it could make the code smaller and more reliable. Ideally we would not need mn -c to clean up state after Mininet was interrupted or a script crashed.

**Expected results**: A version of Mininet which uses the with statement and automatically handles exceptions and cleanup.

**Knowledge prerequisite**: Understanding of Mininet API and internals, Python programming, understanding of underlying Mininet infrastructure (Linux, Open vSwitch, etc..)

### Measured scalability results (and possibly improved scalability)

**Brief explanation**: Mininet's original goal was "1000 nodes on your laptop" but such networks aren't really practical. There's no reason for this - the problem is that the existing implementation has too much overhead. We should measure scalability, profile the system, and identify possible ways of improving scalability. Notably, 1000-node networks are very slow to start up, in part because veth pair creation is slow and adding interfaces to OVS switches gets slower and slower the more switches you have!!

**Expected results**: Reproducible scalability test and analysis scripts for Mininet, as well as understanding and performance debugging of the whole system, hopefully resulting in a version of the system with improved scalability on a single system.

**Knowledge prerequisite**: Understanding of the Mininet internals, C/Linux/system calls/network namespaces, systems programming, and performance analysis at both user and kernel level. Likely systems programming of Open vSwitch and the Linux kernel.

### Provisioning advice and/or automatic provisioning support

**Brief explanation**: Students in CS244 ran into problems when they overcommitted the system. Currently we don't provide much in the way of provisioning guidance, warnings, or monitoring to determine when the system is overcommitted. It would be nice to do all three! Ideally the system could be run in a performance-accurate mode where it would try to guarantee that it was provisioned correctly and provide some kind of alarm or warning when things were going bad. Which leads us to the following....

### Integrated (emulator and emulated) performance monitoring

**Brief explanation**: We developed some performance monitoring code and tools for Mininet 2.0, CS244 and the CoNEXT paper, but these are in a separate source tree and are not currently integrated into the code base. What can we do to add monitoring code to guarantee that important emulation invariants are not being violated, and also to monitor both the performance of the emulator itself and the emulated system?

**Expected results**: Easy installation for Mininet performance monitoring tools, along with examples, documentation and tutorials.

**Knowledge prerequisite**: Understanding of the Mininet internals, C/Linux/system calls/network namespaces, systems programming, and performance analysis.


### Mininet validation against hardware testbeds

**Brief explanation**: We have some benchmarks, but we don't really have a definitive answer as to how far Mininet results match reality. Ideally we would have a deep understanding of Mininet's performance accuracy, a thorough evaluation and comparison to hardware, and validation both against hardware and against invariants that should hold during emulation.

**Expected results**: Scripts for reproducible automated performance tests and summarization/plotting of test results, from microbenchmarks to macrobenchmarks, on both Mininet and hardware testbeds; analysis and explanations of performance discrepancies, and hopefully fixes to improve Mininet's performance accuracy as needed.

**Knowledge prerequisite**: Understanding of the Mininet internals, C/Linux/system calls/network namespaces, systems programming and performance analysis at user and kernel level.

### Other OS support: Debian Wheezy, Fedora Core, BSD? OS X? Windows?

**Brief explanation**: .deb and .rpm install images in addition to PPA, and possibly versions for BSD, OS X, Windows???

Right now we're strongly in the Ubuntu camp. We can almost run out of the box on Debian Wheezy. Fedora Core installation would require modification to the install script. BSD is actually possible now that it has L2 virtual Ethernet and Open vSwitch. Perhaps even OS X is a possibility, although the requisite BSD subsystems (see netmap and VALE) would need to be ported somehow since I don't think they're included in the Xnu/Darwin kernel by default. 

**Difficulty**: Trivial to Very Hard.

**Expected results**: Installation packages and/or VM images for various operating systems other than Ubuntu.

**Knowledge prerequisite**: Understanding of the Mininet internals, C/Linux/system calls/network namespaces, Python systems programming, and systems programming/internals for the target OS.

### Link (e.g. wire or wireless) simulator support

**Brief explanation**: It would be nice to have a link emulator subclass of Link and at least one link simulator, even a simple C (or Python) program that simply does packet forwarding with delay and loss. Ideally we could support a simple wireless link emulator.

**Expected results**: At least one new Mininet class for a link simulator, and integration of a link (e.g. wireless) simulator.

**Knowledge prerequisite**: Understanding of Mininet node.py API and Python programming. C programming and network link modeling/simulation.

### Ability to more compactly package Mininet networks and download into VM

**Brief explanation**: It would be nice to be able to compactly package Mininet experiments without requiring a whole VM. On the other hand, VMs are guaranteed to work! There is a system (whose name I forget) on Linux which packages up applications with their libraries and support files in such a way as to be independent of the underlying OS. Debian packages are similar. Perhaps we could figure out a compact way to package up a whole Mininet system.

**Expected results**: A compact (< 80 MB) VM which is ideally sufficient to complete the OpenFlow tutorial. Scripts to reliably create that VM in an automated fashion.

**Knowledge prerequisite**: Understanding of Mininet (completion of OpenFlow tutorial at least), and understanding of Linux distributions and packaging.

### "Pure" Python implementation (need to determine the performance hit)

**Brief explanation**: Although Mininet cannot truly be implemented in pure Python (it depends on features in the underlying OS), we can rewrite mnexec as Python code (this is what Piconet did as well.) However, we should measure the performance of mnexec vs. Python implementation of same.

**Expected results**: A version of Mininet which replaces the `mnexec` tool with pure Python and runs directly from source on Linux.

**Knowledge prerequisite**: Understanding of the Mininet internals, C/Linux/system calls/network namespaces, and Python systems programming.

### Enhanced unit tests

**Brief explanation**: Right now we don't have a whole lot in terms of unit tests. Ideally we should test all API calls and get some degree of coverage for all of Mininet.

**Expected results**: Additional unit test scripts, and some measure of API/code coverage (preferably tests of each method.)

**Knowledge prerequisite**: Understanding of Linux/IP networking, OpenFlow, Open vSwitch, VM network bridging, the Mininet API, Python, makefiles, shell scripting, and test design including use of coverage tools. Completion of Mininet and OpenFlow tutorials.

### Enhanced system tests

**Brief explanation**: Mininet is great for system-level testing, but ironically we only have a couple of system-level tests that we use to test Mininet itself!! We should test all of our topologies, our switch classes, and various other subsystems like the CLI, command-line argument parsing, performance isolation, and cluster mode.

**Expected results**: A test script and make target incorporating system-level tests for all of the above.

**Knowledge prerequisite**: Understanding of Linux/IP networking, OpenFlow, Open vSwitch, VM network bridging, the Mininet API, Python, makefiles, shell scripting and test design. Completion of Mininet and OpenFlow tutorials.

### Automatic testing of examples/

**Status**: Implemented in 2.1.0.

**Brief explanation**: Not only do we want to be confident that changes to Mininet don't break our examples, but the examples themselves can be thought of as system-level tests which can and should be integrate into automated testing.

**Expected results**: A test script in tests/ and a make target which automatically runs all examples as system-level tests.

**Knowledge prerequisite**: Understanding of Linux/IP networking, OpenFlow, Open vSwitch, VM network bridging, the Mininet API, Python, makefiles, and shell scripting. Completion of Mininet and OpenFlow tutorials.

### Performance analysis and fixes to the Linux kernel and Open vSwitch

**Brief explanation**: We really haven't adequately profiled the whole system, and it's tricky to do so. I expect there are some low-hanging fruit in both Linux and OVS which could be tackled to greatly improve Mininet's performance. In particular, I'd like to see (much) faster startup for large networks.

**Expected results**:  Performance analysis of Mininet and a version which is demonstrably faster and/or more accurate.

**Knowledge prerequisite**: Understanding of Linux/IP networking, VM network bridging, Mininet and Python. Understanding of Linux kernel and user performance tools and performance debugging. C user and kernel programming. Familiarity with simulation. Significant experience with systems programming, simulation/emulation, and performance analysis.


### Virtual time via time-dilation

**Brief explanation**: What sets Emulation apart from Simulation is that usually Emulation runs in wall-clock time rather than having a strong notion of virtual time. Time Dilation is a strategy to allow the emulator's notion of time to progress more slowly than real time, allowing for faster links and computational elements to be simulated than can be simulated running in actual real time. This could enable larger networks to be simulated, or faster components (e.g. 100 GBps interfaces or 10 GHz processors.)

**Expected results**:  A complete Mininet system (installable and as a VM) which has the ability to run in time dilation mode for faster hosts or networks. Tests, documentation, and performance analysis/validation of the system.

**Knowledge prerequisite**: Understanding of Linux/IP networking, VM network bridging, Mininet and Python. Understanding of Linux kernel and user performance tools and performance debugging. C user and kernel programming. Familiarity with simulation. Significant experience with systems programming, simulation/emulation, and performance analysis.

### Virtual time via barrier synchronization

**Brief explanation**: Another approach to virtual time is to allow individual hosts to have separate notions of virtual time, and to pause or slow down hosts which are executing too quickly to allow slower hosts to catch up. Why is this potentially better than time dilation? Because it allows us to arbitrarily instrument certain hosts with time-consuming monitoring or other processing which might slow them down relative to the rest of the system. Note however that the synchronization is approximate - we cannot, for example, synchronize after every instructione (at least not without absurdly impractical overhead.)

**Expected results**:  Performance analysis of Mininet and a version which is demonstrably faster and/or more accurate.

**Knowledge prerequisite**: Understanding of Linux/IP networking, VM network bridging, Mininet and Python. Understanding of Linux kernel and user performance tools and performance debugging. C user and kernel programming. Familiarity with simulation. Experience with distributed systems programming and performance analysis.

### Different modes of operation to trade of emulation speed vs. performance accuracy

**Brief explanation**: Speed vs. detail is a classical trade-off in emulators and simulators. One question is: can we make Mininet faster by sacrificing some performance accuracy. Another is: can we sacrifice some emulation speed to gain more performance accuracy. Another is: can we improve both simulator performance and performance accuracy at the same time?

**Expected results**:  Performance analysis of Mininet and a version which is demonstrably faster and/or more accurate.

**Knowledge prerequisite**: Understanding of Linux/IP networking, VM network bridging, Mininet and Python. Understanding of Linux kernel and user performance tools and performance debugging. C user and kernel programming. Familiarity with simulation. Significant experience with systems programming, simulation/emulation, and performance analysis.

### Higher-performing switches (e.g. VALE-enabled OVS and/or custom switch)

**Brief explanation**: OVS is slow. VALE, in comparison, gets 70 GBps (!!!!) of switching bandwidth on a 1 GHz system. We should be able to do much, much better than we are currently doing, possibly by using the VALE-enabled OVS or creating a custom switch (megaswitch) which is optimized for performance and lives in a single address space. We might be able to trade off some emulation accuracy for performance as welll (e.g. simplified switch vs. OVS, shared memory vs. veth pairs, etc..) Note that VALE runs on both BSD and Linux, but requires a custom Linux kernel. Note that the BSD jail enhancements open up the intriguing possibility of Mininet on BSD and/or OS X (with additional work - see above.)

**Expected results**: A version of Mininet which works with VALE, preferably an OpenFlow-enabled version!

**Knowledge prerequisite**: Understanding of Linux/IP networking, VM network bridging, C programming, Mininet and Python. Familiarity with BSD as well as Linux. Understanding of Linux/BSD kernel building and modules.

### Support for private /etc directory and possbly private filesystem, user space, PID space, etc.

**Status**: Private dirs implemented in `bind.py` example. PID spaces and other features are not yet available.

**Brief explanation**: Although lightweight virtualization is one of Mininet's most compelling features, sometimes it is useful for hosts to have more private data. One example is programs like apache or sshd which expect to have their configuration in /etc. It should be relatively easily to allow hosts to have private /etc directories by using bind mounts, but getting this to work in a convenient and semi-automatic manner may be tricky. Additionally, it may be desirable to allow Mininet  hosts to have private user and PID spaces (although shared user and PID spaces are obviously quite convenient as well.) It should not be terribly difficult to allow these options to be configured both in Mininet() and via the command line.


**Expected results**: A command-line option for `mn` and an API for specifying and managing per-host private directories.

**Knowledge prerequisite**: Understanding of Linux and filesystem mounting, familiarity with Mininet API, code base and Python.