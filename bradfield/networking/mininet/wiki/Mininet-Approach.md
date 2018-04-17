#### The Mininet Approach to Network Research and Prototyping

Mininet was conceived as a way to make it easy to do network research using OpenFlow.

It is based on several guiding ideas and principles:

* It should be easy and fun to create OpenFlow networks / software-defined networks
* Individual researchers and students should be able to easily create and experiment with networks on a single laptop
* Current laptops should be able to create very large experimental networks (with 1990s-class performance ;-) )
* Current clusters should be able to simulate enterprise-class (e.g. 25,000 nodes or more) networks
* Network topologies should be easy to create by specifying simple _parameters_
* Python is (or should be!) simpler than XML for specifying network configurations
* A single network console that can control an entire network is better than hundreds of `xterm` or `ssh` sessions
* Full virtualization is overkill for most applications
* Network systems and experiments should be easy to share, download, and reproduce
* Network designs should move seamlessly from emulation to running at full speed/line rate on hardware
Although Mininet was designed for OpenFlow networks, it also supports legacy IP networking, e.g. using Open vSwitch or an !OpenFlow controller that supports standard Ethernet switching and IP routing.
