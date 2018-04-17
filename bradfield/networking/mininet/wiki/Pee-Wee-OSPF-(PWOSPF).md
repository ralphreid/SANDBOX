## Important Links
* [PWOSPF specification](http://yuba.stanford.edu/cs344/admin/pwospf/)
* [Assignment FAQ](http://yuba.stanford.edu/vns/?page_id=75)
* [Using your sr router with the PWOSPF assignment](http://yuba.stanford.edu/vns/assignments/pwospf/adding-ospf-functionality-to-your-sr-router/)

## Introduction
This assignment involves building advanced functionality on top of a basic VNS router. The goal is to develop a simple dynamic routing protocol, PWOSPF, so that your router can generate its forwarding table automatically based on routes advertised by other routers on the network. By the end of this project, your router is expected to be able to build its forwarding table from link-state advertisements sent from other routers, and route traffic through complex topologies containing multiple nodes.

## PWOSPF
The routing protocol you will be implementing is a link state protocol that is loosely based on OSPFv2. You may find a full specification of PWOSPF [here](http://yuba.stanford.edu/cs344/pwospf/). Note that while PWOSPF is based on OSPFv2 it is sufficiently different that referring to the OSPFv2 as a reference will not be of much help and contrarily may confuse or mislead you.

## Topology and Requirements Overview

The topology of PWOSPF is as follows. There are three routers inter-connected with each other. Client connects to the network through vhost1; Server1 connects to the network through vhost2; Server2 connects to the network through vhost3.

![Topology for PWOSPF](images/pwospf_topo.png)

Your task is to implement PWOSPF within your router so that your router will be able to do the following:

* Build the correct forwarding tables on the assignment topology
* Detect when routers join/or leave the topology and correct the forwarding tables correctly
* Inter-operate with a third party reference solution that implements pwosp

## Implementation Guidance
You are welcome to support PWOSPF in whatever manner you find appropriate. However, to help you get started, we’ve made available modified stub code that creates a PWOSPF subsystem structure within struct **sr_instance** and starts thread that can be used to implement the necessary timer infrastructure. The stub code also includes a header file **pwospf_protocol.h** which may contain useful definitions. You will use the same environment that we setup in "simple router" for this assignment. For detailed instructions, please refer to [[Environment Setup]] and [[Simple Router]].

_**Note: Make sure your EC2 Machine's Security Group opens ports 8888 and 2300. Otherwise, your routers will not be able to communicate with each other.**_

### Download Skeleton Code
Boot up your machine setup with Mininet. Open up a terminal on the machine, download the skeleton code for "PWOSPF" using git.
```no-highlight
> cd ~
> git clone https://huangty@bitbucket.org/huangty/pwospf.git
> cd pwospf
```

The skeleton code resides in pwospf_stub/. If you have implemented "Simple Router", you should make a copy of your "Simple Router" into the pwospf/ directory as follows:

```no-highlight
> pwd
/home/ubuntu/pwospf
> rm -rf pwospf_stub
> cp -r ~/cs144_lab3/router ./pwospf_stub
> cd ./pwospf_stub
> ln -s ../auth_key 
> ln -s ../rtable.vhost1 
> ln -s ../rtable.vhost2
> ln -s ../rtable.vhost3
```
If you would like to build on top of your existing sr router, take a look at these instructions: [Using your sr router with the PWOSPF assignment](http://yuba.stanford.edu/vns/assignments/pwospf/adding-ospf-functionality-to-your-sr-router/)
### Test Connectivity of Your Emulated Topology
We also provide a reference implementation (binary) for you to test the environment. 
#### Configure the Environment
First, configure the environment by running the following command.
```no-highlight
> ./config.sh
```
#### Start Mininet
```no-highlight
> ./run_mininet.sh
```
You should see an output that looks like this (except for the IP addresses).
```
*** Shutting down stale SimpleHTTPServers  
*** Shutting down stale webservers  
server1 192.168.2.200
server2 172.24.3.30
client 10.0.1.100
vhost1-eth1 10.0.1.1
vhost1-eth2 10.0.2.1
vhost1-eth3 10.0.3.1
vhost2-eth1 10.0.2.2
vhost2-eth2 192.168.2.2
vhost2-eth3 192.168.3.1
vhost3-eth1 10.0.3.2
vhost3-eth2 172.24.3.2
vhost3-eth3 192.168.3.2
*** Successfully loaded ip settings for hosts
 {'vhost1-eth2': '10.0.2.1', 'vhost1-eth3': '10.0.3.1', 'server2': '172.24.3.30', 'server1': '192.168.2.200', 'vhost3-eth3': '192.168.3.2', 'vhost3-eth1': '10.0.3.2', 'vhost3-eth2': '172.24.3.2', 'client': '10.0.1.100', 'vhost2-eth3': '192.168.3.1', 'vhost2-eth2': '192.168.2.2', 'vhost2-eth1': '10.0.2.2', 'vhost1-eth1': '10.0.1.1'}
*** Creating network
*** Creating network
*** Adding controller
*** Adding hosts:
client server1 server2 
*** Adding switches:
vhost1 vhost2 vhost3 
*** Adding links:
(client, vhost1) (server1, vhost2) (server2, vhost3) (vhost1, vhost2) (vhost1, vhost3) (vhost2, vhost3) 
*** Configuring hosts
client server1 server2 
*** Starting controller
*** Starting 3 switches
vhost1 vhost2 vhost3 
*** setting default gateway of host server1
server1 192.168.2.2
*** setting default gateway of host server2
server2 172.24.3.2
*** setting default gateway of host client
client 10.0.1.1
*** Starting SimpleHTTPServer on host server1 
*** Starting SimpleHTTPServer on host server2 
*** Starting CLI:
```

#### Start POX
Start the Mininet controller (and wait for it to print some messages)
```no-highlight
> ./run_pox.sh
```

It will print messages that look like this:
```
POX 0.0.0 / Copyright 2011 James McCauley
server1 192.168.2.200
server2 172.24.3.30
client 10.0.1.100
vhost1-eth1 10.0.1.1
vhost1-eth2 10.0.2.1
vhost1-eth3 10.0.3.1
vhost2-eth1 10.0.2.2
vhost2-eth2 192.168.2.2
vhost2-eth3 192.168.3.1
vhost3-eth1 10.0.3.2
vhost3-eth2 172.24.3.2
vhost3-eth3 192.168.3.2
DEBUG:.home.ubuntu.pwospf.pox_module.pwospf.ofhandler:*** ofhandler: Successfully loaded ip settings for hosts
 {'vhost1-eth2': '10.0.2.1', 'vhost1-eth3': '10.0.3.1', 'server2': '172.24.3.30', 'server1': '192.168.2.200', 'vhost3-eth3': '192.168.3.2', 'vhost3-eth1': '10.0.3.2', 'vhost3-eth2': '172.24.3.2', 'client': '10.0.1.100', 'vhost2-eth3': '192.168.3.1', 'vhost2-eth2': '192.168.2.2', 'vhost2-eth1': '10.0.2.2', 'vhost1-eth1': '10.0.1.1'}

INFO:.home.ubuntu.pwospf.pox_module.pwospf.srhandler:created server
DEBUG:.home.ubuntu.pwospf.pox_module.pwospf.srhandler:SRServerListener listening on 8888
DEBUG:core:POX 0.0.0 going up...
DEBUG:core:Running on CPython (2.7.3/Aug 1 2012 05:14:39)
INFO:core:POX 0.0.0 is up.
This program comes with ABSOLUTELY NO WARRANTY.  This program is free software,
and you are welcome to redistribute it under certain conditions.
Type 'help(pox.license)' for details.
DEBUG:openflow.of_01:Listening for connections on 0.0.0.0:6633
Ready.
POX> INFO:openflow.of_01:[Con 1/1] Connected to 00-00-00-00-00-01
DEBUG:.home.ubuntu.pwospf.pox_module.pwospf.ofhandler:Connection [Con 1/1]
{'vhost1': {'eth3': ('10.0.3.1', 'fe:0c:ce:98:e6:c1', '10Gbps', 3)}}
{'vhost1': {'eth3': ('10.0.3.1', 'fe:0c:ce:98:e6:c1', '10Gbps', 3), 'eth2': ('10.0.2.1', 'ca:2a:c3:0a:c8:48', '10Gbps', 2)}}
{'vhost1': {'eth3': ('10.0.3.1', 'fe:0c:ce:98:e6:c1', '10Gbps', 3), 'eth2': ('10.0.2.1', 'ca:2a:c3:0a:c8:48', '10Gbps', 2), 'eth1': ('10.0.1.1', '36:fa:7f:22:db:65', '10Gbps', 1)}}
DEBUG:.home.ubuntu.pwospf.pox_module.pwospf.srhandler:SRServerListener catch RouterInfo even for vhost=vhost1, info={'eth3': ('10.0.3.1', 'fe:0c:ce:98:e6:c1', '10Gbps', 3), 'eth2': ('10.0.2.1', 'ca:2a:c3:0a:c8:48', '10Gbps', 2), 'eth1': ('10.0.1.1', '36:fa:7f:22:db:65', '10Gbps', 1)}, rtable=[('10.0.1.100', '10.0.1.100', '255.255.255.255', 'eth1'), ('10.0.2.0', '10.0.2.2', '255.255.255.0', 'eth2'), ('10.0.3.0', '10.0.3.2', '255.255.255.0', 'eth3')]
INFO:openflow.of_01:[Con 3/3] Connected to 00-00-00-00-00-03
DEBUG:.home.ubuntu.pwospf.pox_module.pwospf.ofhandler:Connection [Con 3/3]
{'vhost3': {'eth3': ('192.168.3.2', '02:1a:66:94:d6:94', '10Gbps', 3)}}
{'vhost3': {'eth3': ('192.168.3.2', '02:1a:66:94:d6:94', '10Gbps', 3), 'eth2': ('172.24.3.2', 'be:b8:be:fd:23:25', '10Gbps', 2)}}
{'vhost3': {'eth3': ('192.168.3.2', '02:1a:66:94:d6:94', '10Gbps', 3), 'eth2': ('172.24.3.2', 'be:b8:be:fd:23:25', '10Gbps', 2), 'eth1': ('10.0.3.2', '06:28:51:f8:1f:93', '10Gbps', 1)}}
DEBUG:.home.ubuntu.pwospf.pox_module.pwospf.srhandler:SRServerListener catch RouterInfo even for vhost=vhost3, info={'eth3': ('192.168.3.2', '02:1a:66:94:d6:94', '10Gbps', 3), 'eth2': ('172.24.3.2', 'be:b8:be:fd:23:25', '10Gbps', 2), 'eth1': ('10.0.3.2', '06:28:51:f8:1f:93', '10Gbps', 1)}, rtable=[('10.0.3.0', '10.0.3.1', '255.255.255.0', 'eth1'), ('172.24.3.30', '172.24.3.30', '255.255.255.255', 'eth2'), ('192.168.3.0', '192.168.3.1', '255.255.255.0', 'eth3')]
INFO:openflow.of_01:[Con 2/2] Connected to 00-00-00-00-00-02
DEBUG:.home.ubuntu.pwospf.pox_module.pwospf.ofhandler:Connection [Con 2/2]
{'vhost2': {'eth3': ('192.168.3.1', 'de:4a:68:6f:57:24', '10Gbps', 3)}}
{'vhost2': {'eth3': ('192.168.3.1', 'de:4a:68:6f:57:24', '10Gbps', 3), 'eth2': ('192.168.2.2', '7e:85:b3:94:93:91', '10Gbps', 2)}}
{'vhost2': {'eth3': ('192.168.3.1', 'de:4a:68:6f:57:24', '10Gbps', 3), 'eth2': ('192.168.2.2', '7e:85:b3:94:93:91', '10Gbps', 2), 'eth1': ('10.0.2.2', 'be:a6:3e:d3:3c:a2', '10Gbps', 1)}}
DEBUG:.home.ubuntu.pwospf.pox_module.pwospf.srhandler:SRServerListener catch RouterInfo even for vhost=vhost2, info={'eth3': ('192.168.3.1', 'de:4a:68:6f:57:24', '10Gbps', 3), 'eth2': ('192.168.2.2', '7e:85:b3:94:93:91', '10Gbps', 2), 'eth1': ('10.0.2.2', 'be:a6:3e:d3:3c:a2', '10Gbps', 1)}, rtable=[('10.0.2.0', '10.0.2.1', '255.255.255.0', 'eth1'), ('192.168.2.200', '192.168.2.200', '255.255.255.255', 'eth2'), ('192.168.3.0', '192.168.3.2', '255.255.255.0', 'eth3')]
```

#### Start Reference Solution

##### Running Multiple Routers
Because this assignment requires multiple instances of your router to run simultaneously you will want to use the -r and the -v command line options. -r allows you to specify the routing table file you want to use (e.g. -r rtable.vhost1) and -v allows you to specify the host you want to connect to on the topology (e.g. -v vhost3). We also provide a script (run_sr.sh) to help you to run multiple instances of sr. Note that, **You have to run each sr on a different machine, since they all bind to the same port.**

First, you will need to figure out the IP of your machine runs Mininet/POX:
```no-highlight
> curl ifconfig.me
A.B.C.D
```
A.B.C.D will be your public IP. 

Now, on the same machine, connect your reference solution, sr_solution, to vhost1. Replace A.B.C.D with the actual IP of your Mininet/POX machine.
```no-highlight
> ./run_sr.sh A.B.C.D vhost1
```

It will print messages that look like this:
```
Initializing the router subsystem
Initializing the router work queue with 1 worker threads
handling buckets on the wait list
Nothing to do, will sleep until next event in 1s, 0ns
waiting for expected messages ...
successfully authenticated as ubuntu
got expected messages ...
Received Hardware Info with 18 entries
Interface: eth3
Speed: 0
Hardware Address: fe:0c:ce:98:e6:c1
Ethernet IP: 10.0.3.1
Subnet: 0.0.0.0
Mask: 255.255.255.0
Interface: eth2
Speed: 0
Hardware Address: ca:2a:c3:0a:c8:48
Ethernet IP: 10.0.2.1
Subnet: 0.0.0.0
Mask: 255.255.255.0
Interface: eth1
Speed: 0
Hardware Address: 36:fa:7f:22:db:65
Ethernet IP: 10.0.1.1
Subnet: 0.0.0.0
Mask: 255.255.255.0
Performing post-hw setup initialization
Loading routing table from rtable.vhost1
2300
Sending PWOSPF HELLOs
Ethernet frame sent successfully (arp_cache_handle_partial_frame)
Ethernet frame sent successfully (arp_cache_handle_partial_frame)
Ethernet frame sent successfully (arp_cache_handle_partial_frame)
Sending PWOSPF UPDATEs: 6 (104)
ADVERTS BEING SENT OUT (seq=0) (advert)
  advert: 10.0.3/24 0.0.0.0
  advert: 10.0.2/24 0.0.0.0
  advert: 10.0.1/24 0.0.0.0
  advert: 10.0.1.100/32 0.0.0.0
  advert: 10.0.2/24 0.0.0.0
  advert: 10.0.3/24 0.0.0.0
 ==> 10.0.3/24  ... added to list
 ==> 10.0.2/24  ... added to list
 ==> 10.0.1/24  ... added to list
 ==> 10.0.1.100/32  ... added to list
 ==> 10.0.2/24  ... already in list
 ==> 10.0.3/24  ... already in list
Sending PWOSPF UPDATEs
destroy topo
prune missing routes
update rtable
next loop!
Nothing to do but sleep for 5 seconds
handling buckets on the wait list
Nothing to do, will sleep until next event in 1s, 0ns
```

**If you don't see any IP settings loaded in, please check if your machine's port 8888 and 2300 is opened for connection.**

Now, on a different machine, connect your reference solution, sr_solution, to vhost2. Replace A.B.C.D with the actual IP of your Mininet/POX machine.
```no-highlight
> ./run_sr.sh A.B.C.D vhost2
```
You should see a similar output. 

On yet another different machine, connect your reference solution, sr_solution, to vhost3. Replace A.B.C.D with the actual IP of your Mininet/POX machine.
```no-highlight
> ./run_sr.sh A.B.C.D vhost3
```
You should see a similar output. 

Now, back to the Mininet CLI to send some ping packets from client to server1:
```no-highlight
mininet> client ping -c 3 192.168.2.200
```
On the Mininet CLI, you should be able to see the following output:
```
PING 192.168.2.200 (192.168.2.200) 56(84) bytes of data.
64 bytes from 192.168.2.200: icmp_req=1 ttl=62 time=276 ms
64 bytes from 192.168.2.200: icmp_req=2 ttl=62 time=120 ms
64 bytes from 192.168.2.200: icmp_req=3 ttl=62 time=138 ms

--- 192.168.2.200 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2002ms
rtt min/avg/max/mdev = 120.097/178.280/276.351/69.749 ms
```

Congratulations, you have successfully setup and tested your emulated topology! You are now ready to code!

## Dealing With Routes

The [[Simple Router]] project does not really require sophisticated handling of routes. However, when implementing pwospf, special care must be taken to ensure that routes are treated correctly by your router. Before starting pwospf development, we suggest that you first ensure your router properly handles default routes, gateways and subnets.

### Next Hop
The routing table consists of 3 fields; destination prefix, next-hop, network mask and the outgoing interface. The next-hop specifies the IP address of the next hop router towards the destination. What if the destination is directly connected to one of the router’s interfaces? In this case, the next-hop value is 0 (0.0.0.0) serving as an indication to the router that the packets destination address is directly connected to outgoing interface specified by the route. If your router receives a packet to destination 1.2.3.4 and your router has a route:
1.2.3.0 0.0.0.0 255.255.255.0 eth1
Your router should use 1.2.3.4 as the next hop out of eth1.

### Subnets (and longest prefix mask)
The subnet-mask field of the routing table specifies the size of the subnet being routed to. More specifically, given a particular destination IP addresses (ipdest), it matches with a route if (ipdest & mask) equals (dest & mask) (typically the destination prefix in the routing table is started as (dest & mask) so &’ing with the mask is unnecessary). It is important to note that a given destination IP address can match with multiple subnets (in fact this is often the case). For example, all destinations match the default route ((ipdest & 0) = 0)! In these cases, the router must choose the best or most specific match. This is done by selecting the match with the longest prefix or the largest value subnet mask. Because you will be updating your forwarding table dynamically, you will need to find an (efficient) method for supporting longest prefix match rather than just selecting the first route that matches. *Be sure to consider the subnet mask when handling routes.*

### Static vs. Dynamic Routes
During operation, your routing table should contain both static and dynamic routes. Static routes are read in from the routing table (rtable) and should never be removed or modified. Dynamic routes are added/removed by your PWOSPF implementation. You must therefore keep track of which routes are static. You handle this however you like, e.g. maintaining two separate tables, or marking routes as static/dynamic. For consistency your router must always select dynamic routes over static routes regardless of prefix size.

## Control Path Versus Forwarding Path
High end hardware routers and software routing daemons (such as routed, zebra and xorp) abstract the control functionality of the router such as management, and routing protocols away from the forwarding functionality. The forwarding path should do just that, forwarding. The control path, on the other hand, tries to figure out what the particular configuration of the forwarding path should be and updates the forwarding path periodically. Typically, the configuration functionality will maintain copies of the forwarding path data structures (such as the routing table) and use those for updates. You have already developed a usable forwarding path in the basic router assignment. In this project you will build a control path on top of that to update the routing table based on the calculated shortest path to each reachable subnet.

## What Routes to Advertise
Your router is responsible for advertising all of its static routes along with the subnets connected to each of its interfaces. Given any router on the network, aggregating all of this information properly should create a subnet graph from which you can calculate the correct routing table for that router to each of the advertised subnets. Exactly how to do this is part of the assignment challenge.

## Some Pitfalls
Be careful not to add a route in your routing table for subnets directly connected to one of your interfaces even if these subnets are being advertised (in most cases they will be e.g. if there is another router on the subnet).

You will almost certainly need to use threads in this assignment to support the periodic updates (e.g. HELLO packets). Be careful to avoid race conditions. Your routing table in particular will be need to be locked off so that you don’t fall of the end when looking up a route for a packet during updates.

Testing in this assignment can be difficult. You may want to add code to your router so than you can disable an interface at run time. You can use this to test whether your implementation converges after a link goes down (e.g. if the link between vhost1 and vhost2 goes down, server1 should still be reachable on the path vhost1 -> vhost3 -> vhost2 -> server1).

## Expected Functionality
Your router should be able to build the correct routing tables and route traffic to the application servers on the assignment topology. Specifically, we expect to be able to start three instances of your router with the only static route being the default route on vhost1 and then be able to reach app1 and app2 within a reasonable amount of time. Your router should be able to correct the routing tables if a link goes down (such as the link between vhost1 and vhost2). We will likely test this by modifying the stub code to drop all packets out of a particular interface after a given time period.
















