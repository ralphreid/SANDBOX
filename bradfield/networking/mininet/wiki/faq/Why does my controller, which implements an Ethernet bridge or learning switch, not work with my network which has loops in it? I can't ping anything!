### Why does my controller, which implements an Ethernet bridge or learning switch, not work with my network which has loops in it? I can't ping anything!

It doesn't work because your network has loops in it.

Transparent bridging of L2/Ethernet networks doesn't work if the topology has loops in it, for a variety of reasons: ARP does broadcasts, packets are flooded by default, learning switches don't deal well with seeing the same MAC address on multiple ports and could potentially learn a route to themselves, and Ethernet frames don't have a time to live field (TTL) like IP packets (otherwise flooding might work, if inefficiently.) As a result, many Ethernet bridges implement variants of a Spanning Tree Protocol (STP), which simply deactivates links in the network to remove loops. Of course, this also throws away network bandwidth that you could otherwise be using, and creates a bottleneck at the root of the tree.

The OpenFlow reference controller (`controller`) implements a bridge/learning switch, as does NOX's `pyswitch` module.

In general, if you want to use a network with loops in it, you need to be absolutely sure that your controller supports such a network. As mentioned above, `controller` and `pyswitch` do not by default. NOX has a `spanning_tree` module, which you may wish to investigate.


